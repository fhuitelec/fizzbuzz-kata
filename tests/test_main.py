"""Test module for the FizzBuzz kata."""

import pytest

from fizzbuzz.main import hello_world


@pytest.mark.parametrize(("number"), [(1), (2)])
def test_hello_world(number):
    """Dummy test."""
    assert hello_world() == "Hello world!"
    assert number == number  # pylint: disable=comparison-with-itself
