"""
Tests the hello module.
"""

import hello1234


def test_hello_no_name():
    """
    Checks that if no name is passed, we get "Hello, World"
    """
    assert hello1234.hello() == 'Hello, World'


def test_hello_with_name():
    """
    If passed a name, return, "Hello, name"
    """
    assert hello1234.hello('Nicholas') == 'Hello, Nicholas'
