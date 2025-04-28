"""Test module for the FizzBuzz kata."""

import pytest

from fizzbuzz.main import fizz_buzz, generate_fizz_buzz_string, hello_world


@pytest.mark.parametrize(("number"), [(1), (2)])
def test_hello_world(number):
    """Dummy test."""
    assert hello_world() == "Hello world!"
    assert number == number  # pylint: disable=comparison-with-itself


@pytest.mark.parametrize(("number"), [(1), (2), (7), (19)])
def test_regular_number_returns_the_number(number):
    """Test."""
    result = fizz_buzz()
    assert result[number - 1] == str(number)


@pytest.mark.parametrize(("number"), [(3), (30), (42), (90)])
def test_multiple_of_3_returns_fizz(number):
    """Test."""
    result = fizz_buzz()
    assert result[number - 1] == "fizz"


@pytest.mark.parametrize(("number"), [(5), (25), (50), (65)])
def test_multiple_of_5_returns_fizz(number):
    """Test."""
    result = fizz_buzz()
    assert result[number - 1] == "buzz"


def test_fizz_buzz_returns_100_numbers():
    """Test."""
    result = generate_fizz_buzz_string().split("\n")
    assert len(result) == 100
