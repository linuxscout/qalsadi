

## 🧰 Qalsadi Command-Line Interface (CLI)

Qalsadi provides a simple command-line tool to perform **morphological analysis** or **lemmatization** of Arabic text.

### 🔧 Usage

```bash
python -m qalsadi [OPTIONS]
```

### 🏁 Modes

Use the `--mode` option to choose the processing type:

| Mode        | Description                      |
| ----------- | -------------------------------- |
| `analyze`   | Morphological analysis (default) |
| `lemmatize` | Extract base lemma(s) of words   |

---

## 📥 Input Options (one required)

| Option    | Description                    |
| --------- | ------------------------------ |
| `--text`  | Direct input text (quoted)     |
| `--file`  | Path to UTF-8 text file        |
| `--stdin` | Read input from standard input |

---

## 📤 Output Options

| Option      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `--format`  | Output format: `table`, `json`, `csv`, `html`                |
| `--profile` | Output profile for analysis: `main`, `lemmas`, `roots`, etc. |
| `--limit`   | Limit number of words analyzed (default: 10000)              |

> `--profile` is only used in `analyze` mode.

---

## 🧠 Lemmatizer Options

Used only with `--mode lemmatize`:

| Option         | Description                       |
| -------------- | --------------------------------- |
| `--return-pos` | Return part-of-speech with lemmas |
| `--all`        | Return all lemma candidates       |

---

## ✅ Examples

### ➤ Analyze from text (default)

```bash
python -m qalsadi --text "ذهب الطفل إلى المدرسة"
```

### ➤ Explicit analyze mode, HTML output

```bash
python -m qalsadi --mode analyze --text "أحب القراءة" --format html
```

### ➤ Lemmatize from stdin

```bash
echo "الولد يقرأ" | python -m qalsadi --mode lemmatize --stdin --return-pos
```

### ➤ Analyze from file with specific profile

```bash
python -m qalsadi --mode analyze --file examples/input.txt --format table --profile roots
```

---





## 🧰 واجهة سطر الأوامر (CLI) لمكتبة Qalsadi

توفر مكتبة Qalsadi أداة سطر أوامر بسيطة لتحليل النصوص العربية صرفيًا أو لاستخراج جذر الكلمات (lemmatization).

------

### 🏁 الوضع (mode)

استخدم الخيار `--mode` لاختيار نوع المعالجة:

| الوضع (`--mode`) | الوصف                                    |
| ---------------- | ---------------------------------------- |
| `analyze`        | التحليل الصرفي (الوضع الافتراضي)         |
| `lemmatize`      | استخراج الجذر أو الصيغة الأساسية للكلمات |

------

### 📥 خيارات الإدخال (أحدها مطلوب)

| الخيار    | الوصف                                           |
| --------- | ----------------------------------------------- |
| `--text`  | نص مباشر داخل علامات تنصيص                      |
| `--file`  | مسار ملف نصي UTF-8 يحتوي على المحتوى            |
| `--stdin` | قراءة الإدخال من الـ stdin (سطر الأوامر مباشرة) |

------

### 📤 خيارات الإخراج

| الخيار      | الوصف                                                        |
| ----------- | ------------------------------------------------------------ |
| `--format`  | صيغة الإخراج: `table` (افتراضية)، أو `json`، أو `csv`، أو `html` |
| `--profile` | اختيار الحقول المعروضة: `main`، `lemmas`، `roots`، `inflect` |
| `--limit`   | الحد الأقصى لعدد الكلمات المعالجة (الافتراضي: 10000)         |

> ملاحظة: الخيار `--profile` يُستخدم فقط مع الوضع `analyze`.

------

### 🧠 خيارات lemmatize

تُستخدم فقط مع `--mode lemmatize`:

| الخيار         | الوصف                                            |
| -------------- | ------------------------------------------------ |
| `--return-pos` | إرجاع نوع الكلمة (فعل، اسم، ... إلخ) مع الجذر    |
| `--all`        | إرجاع كل الجذور المحتملة وليس فقط الأكثر احتمالًا |

------

## ✅ أمثلة الاستخدام

### ➤ تحليل نص مباشر

```bash
python -m qalsadi --text "ذهب الطفل إلى المدرسة"
```

### ➤ تحديد الوضع وإخراج بصيغة HTML

```bash
python -m qalsadi --mode analyze --text "أحب القراءة" --format html
```

### ➤ استخراج الجذر من stdin

```bash
echo "الولد يقرأ" | python -m qalsadi --mode lemmatize --stdin --return-pos
```

### ➤ تحليل نص من ملف بصيغة جدول وجذر فقط

```bash
python -m qalsadi --mode analyze --file examples/input.txt --format table --profile roots
```

------

