import subprocess
import sys
import os
import pytest

SCRIPT = [sys.executable, "-m", "qalsadi"]

def run_cli(args):
    return subprocess.run(SCRIPT + args, capture_output=True, text=True)

def test_analyze_text_table():
    result = run_cli(["--text", "ذهب الولد إلى المدرسة", "--format", "table"])
    assert result.returncode == 0
    assert "الولد" in result.stdout

def test_analyze_text_json():
    result = run_cli(["--text", "ذهب الولد", "--format", "json"])
    assert result.returncode == 0
    assert result.stdout.strip().startswith("[")

def test_lemmatize_text_json():
    result = run_cli(["--mode", "lemmatize", "--text", "الولد يذهب", "--format", "json"])
    assert result.returncode == 0
    assert result.stdout.strip().startswith("[")

def test_missing_input_fails():
    result = run_cli(["--mode", "analyze"])
    assert result.returncode != 0
    assert "error" in result.stderr.lower()

@pytest.mark.parametrize("profile", ["main", "roots", "lemmas"])
def test_analyze_with_profiles(profile):
    result = run_cli(["--text", "ذهب الطالب", "--format", "table", "--profile", profile])
    assert result.returncode == 0
    assert "ذهب" in result.stdout

def test_stdin_input(monkeypatch):
    input_text = "يكتب الطالب الدرس"
    monkeypatch.setattr("sys.stdin", open(os.devnull, "r"))
    result = subprocess.run(SCRIPT + ["--stdin", "--mode", "lemmatize"], input=input_text, capture_output=True, text=True)
    assert result.returncode == 0
    assert "يكتب" in result.stdout or "كتب" in result.stdout
