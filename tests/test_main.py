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
    fizz_result = fizz_buzz()
    result = fizz_result.split("\n")
    assert result[number - 1] == str(number)

def test_fizz_buzz_returns_100_numbers():
    fizz_result = fizz_buzz()
    result = fizz_result.split("\n")
    assert len(result) == 100
