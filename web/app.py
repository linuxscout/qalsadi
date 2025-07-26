from flask import Flask, request, render_template, send_file, redirect, url_for
from werkzeug.exceptions import RequestEntityTooLarge
from flask import copy_current_request_context
import qalsadi.analex as qa
from qalsadi.resultformatter import ResultFormatter
from qalsadi.abstractresultformatter import AbstractResultFormatter
import io
from pyarabic import araby
from tashaphyne.stemming import ArabicLightStemmer
from qalsadi.lemmatizer import Lemmatizer
import arrand.arrandom  # make sure you install this or mock it
import mimetypes

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB
# Store results in memory (in a real app, use session or DB)
latest_formatter = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_formatter
    results = None
    table = ""
    input_text = ""
    output="JUST A TEST"
    output_format=""
    profile = "main"  # default
    action = ""

    if request.method == 'POST':
        # Handle uploaded file
        uploaded_file = request.files.get('textfile')
        if uploaded_file and allowed_file(uploaded_file.filename) and is_text_file(uploaded_file):
            try:
                input_text = uploaded_file.read().decode('utf-8', errors='ignore')

            except UnicodeDecodeError:
                return "⚠️ الملف ليس نصاً صالحاً بتنسيق UTF-8", 400

        # Otherwise use textarea input
        if not input_text:
            input_text = request.form.get('text', '')
        # Optional: strip HTML/JS characters
        input_text = input_text.replace('<', '').replace('>', '').replace('&', '')

        output_format = request.form.get('format', 'html')
        profile = request.form.get('profile', 'main')  # NEW
        allow_tag_guessing = bool(request.form.get('allow_tag_guessing', ""))
        allow_disambiguation = bool(request.form.get('allow_disambiguation', ""))
        action = request.form.get('action', 'analyze')

        # other actions
        if action !="analyze":
            results = handle_action(action=action, input_text=input_text, output_format=output_format)
            output = results.get("output")
            output_format = results.get("output_format", output_format)
        else:
            @copy_current_request_context
            def run_analysis(text):
                analyzer = qa.Analex(
                        allow_tag_guessing=allow_tag_guessing,
                        allow_disambiguation=allow_disambiguation
                )
                return analyzer.check_text(text)
            qresult = run_analysis(input_text)
            formatter = ResultFormatter(qresult)
            formatter.set_used_fields(profile)  # change profile if needed

            output = formatter.as_format(output_format)
            latest_formatter = formatter


    return render_template('index.html', text=input_text, output=output,
                           format=output_format,
                           selected_profile=profile,
                           action=action)

@app.route('/download/<fmt>')
def download(fmt):
    global latest_formatter
    if not latest_formatter:
        return redirect(url_for('index'))

    if fmt == 'json':
        data = latest_formatter.as_json()
        mime = 'application/json'
        ext = 'json'
    elif fmt == 'csv':
        data = latest_formatter.as_csv()
        mime = 'text/csv'
        ext = 'csv'
    elif fmt == 'xml':
        data = latest_formatter.as_xml()
        mime = 'application/xml'
        ext = 'xml'
    else:
        return "Unsupported format", 400

    # Convert string to bytes and wrap in BytesIO
    byte_io = io.BytesIO(data.encode('utf-8'))
    return send_file(byte_io, mimetype=mime, as_attachment=True,
                     download_name=f'qalsadi_output.{ext}')

@app.errorhandler(413)
@app.errorhandler(RequestEntityTooLarge)
def file_too_large(e):
    return "⚠️ الملف كبير جدًا. الحد الأقصى للحجم هو 1 ميغابايت.", 413

def handle_action(action, input_text="", output_format="", options=[]):
    # Handle each action
    output = ""
    global latest_formatter
    if action == 'stemming':
        stemmed = light_stemmer(input_text)
        # output = "Stemming " + "\n".join([w.__repr__() for w in stemmed])
        formatter = stemmerformatter(stemmed)
        latest_formatter = formatter
        output = formatter.as_format(output_format)
    elif action == 'tokenize':
        output = "<br>".join(araby.tokenize(input_text))
        output_format = "table"
        latest_formatter = None
    elif action == 'sort':
        tokens = araby.tokenize(input_text)
        output = "Sorting \n" + "\n".join(sorted(tokens))
        output_format = "table"
        latest_formatter = None
    elif action == 'strip_tashkeel':
        output = araby.strip_tashkeel(input_text)
        output_format = "table"
        latest_formatter = None
    elif action == 'lemmatize':
        lemmatizer = Lemmatizer()
        words = araby.tokenize(input_text)
        lemmas = lemmatizer.lemmatize_text(input_text)
        output = "Lemmatization " + "<br>".join(lemmas)
        latest_formatter = None
    elif action == 'random_arabic':
        input_text = arrand.arrandom.select()  # or 5 lines etc.
        output = "Random\n" + input_text
        output_format = "table"
        latest_formatter = None
    elif action == 'random_arabic_vocalized':
        input_text = arrand.arrandom.select(vocalized=True)  # or 5 lines etc.
        output = "Random vocalized\n" + input_text
        output_format = "table"
        latest_formatter = None
    return  {"output":output, "output_format":output_format}

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_text_file(file_storage):
    mime_type = mimetypes.guess_type(file_storage.filename)[0]
    return mime_type == 'text/plain'

def light_stemmer(text):
    """
    LightStemming unsing Tashaphyne
    """
    result = []
    als = ArabicLightStemmer()
    word_list = als.tokenize(text)
    for word in word_list:
        #~listseg =  als.segment(word)
        als.segment(word)
        affix_list = als.get_affix_list()
        for affix in affix_list:
            result.append({'word':word, 'prefix':affix['prefix'],
            'stem':affix['stem'], 'suffix':affix['suffix'],
            'root':affix['root'], 'type':'-'}
                          )
    return result

class stemmerformatter(AbstractResultFormatter):
    def __init__(self,results):
        self.results = results
        assert self._is_valid_result_type(results)
        # self.flat_results = [item.__dict__ for sublist in results for item in sublist]
        self.all_fields = self._collect_all_fields()
        self.used_fields = list(self.all_fields)  # default is all

        self.profiles = {
            "main": ["id", "word",  "prefix", "stem", "suffix", "root", "type"],
            "all": self.all_fields,
        }

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
