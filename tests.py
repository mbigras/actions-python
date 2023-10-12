import subprocess

from hello import hello, unix_start


def test_hello():
    assert hello() == "Hello, World!"


def test_main():
    result = subprocess.run(["python", "hello.py"], capture_output=True, text=True)
    assert result.stdout == "Hello, World!\n"


def test_unix_start():
    assert unix_start() == "1970-01-01T00:00:00+00:00"
