from hello_name import hello_name
import pytest

def test_hello_name():
    assert hello_name("Bob") == "hello Boo"
