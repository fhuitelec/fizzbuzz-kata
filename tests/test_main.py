"""Test module for the FizzBuzz kata."""

import pytest

from fizzbuzz.main import fizz_buzz, hello_world


@pytest.mark.parametrize(("number"), [(1), (2)])
def test_hello_world(number):
    """Dummy test."""
    assert hello_world() == "Hello world!"
    assert number == number  # pylint: disable=comparison-with-itself

@pytest.mark.parametrize(("number"), [(1), (2), (7), (19)])
def test_regular_number_returns_the_number(number):
    assert fizz_buzz(number) == str(number)
