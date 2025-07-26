from flask import Flask, request, render_template, send_file, redirect, url_for

from flask import copy_current_request_context
import qalsadi.analex as qa
from qalsadi.resultformatter import ResultFormatter
import io

app = Flask(__name__)
# Store results in memory (in a real app, use session or DB)
latest_formatter = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global latest_formatter
    results = None
    table = ""
    input_text = "السلام عليكم"
    output="JUST A TEST"
    output_format=""
    profile = "main"  # default

    if request.method == 'POST':
        input_text = request.form.get('text', '')
        output_format = request.form.get('format', 'html')
        profile = request.form.get('profile', 'main')  # NEW

        @copy_current_request_context
        def run_analysis(text):
            analyzer = qa.Analex()
            return analyzer.check_text(text)
        qresult = run_analysis(input_text)
        formatter = ResultFormatter(qresult)
        formatter.set_used_fields(profile)  # change profile if needed

        if output_format == 'html':
            output = formatter.as_table(tablefmt="html")
            output =  output.replace('<table>','<table id="datatable">')
        elif output_format == 'json':
            output = formatter.as_json()
        elif output_format == 'csv':
            output = formatter.as_csv()
        elif output_format == 'xml':
            output = formatter.as_xml()
        else:
            output = formatter.as_table()
        latest_formatter = formatter
    return render_template('index.html', text=input_text, output=output,
                           format=output_format,
                           selected_profile=profile)

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


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
