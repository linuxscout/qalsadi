# Contributing to Qalsadi

Thank you for considering contributing to **Qalsadi** – an open-source Arabic morphological analyzer and lemmatizer. Your contributions help make Arabic NLP better for everyone.


## 🛠️ Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/linuxscout/qalsadi.git
   cd qalsadi```


1. (Optional) **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the package in editable mode**:

   ```bash
   pip install -e .[dev]
   ```

------

## 🧪 Running Tests

We use Python's `unittest` (and optionally `pytest`) for testing. Tests are located in the `tests/` directory.

To run tests:

```bash
python3 -m unittest discover tests
# or
pytest
```

------

## 🧼 Code Style

- Follow [PEP8](https://peps.python.org/pep-0008/) coding guidelines.
- Use descriptive names and write docstrings for public methods.
- Avoid commented-out code in commits.

Use `black` to format:

```bash
black qalsadi/ tests/
```

------

## 💡 Submitting Changes

1. Create a new branch:

   ```bash
   git checkout -b feature/my-new-feature
   ```

2. Make your changes and **add tests** if needed.

3. Commit and push:

   ```bash
   git commit -m "Add feature: describe it"
   git push origin feature/my-new-feature
   ```

4. Open a Pull Request from your branch to `main`.

Please describe your changes clearly, and reference any related issues.

------

## 📁 Directory Structure

```
qalsadi/        # Core Python package
tests/          # Unit tests
tests/fixtures/ # Test data
docs/           # Documentation (Markdown or Sphinx)
data/           # Static resources (e.g. database files)
```

------

## 🤝 Code of Conduct

Please be respectful and constructive in all interactions. We're building a welcoming and inclusive community for Arabic NLP.

------

## 🙋 Need Help?

Open an [Issue](https://github.com/linuxscout/qalsadi/issues) or reach out by email at [taha.zerrouki@gmail.com](mailto:taha.zerrouki@gmail.com).

Happy hacking!

– Taha Zerrouki and the Qalsadi contributors

```