"""
Tests the hello module.
"""

import pytest
import hello


def test_hello_no_name():
    """
    Checks that if no name is passed, we get "Hello, World"
    """
    assert hello.hello() == 'Hello, World'

def test_hello_with_name():
    """
    If passed a name, return, "Hello, name"
    """
    assert hello.hello('Nicholas') == 'Hello, Nicholas'
