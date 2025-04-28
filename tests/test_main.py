"""Test module for the FizzBuzz kata."""

import pytest

from fizzbuzz.main import fizz_buzz, generate_fizz_buzz_string, hello_world


@pytest.mark.parametrize(("number"), [(1), (2)])
def test_hello_world(number):
    """Dummy test."""
    assert hello_world() == "Hello world!"
    assert number == number  # pylint: disable=comparison-with-itself


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, "1"),
        (2, "2"),
        (3, "fizz"),
        (5, "buzz"),
        (7, "7"),
        (15, "fizzbuzz"),
        (19, "19"),
        (25, "buzz"),
        (27, "fizz"),
        (30, "fizzbuzz"),
        (42, "fizz"),
        (50, "buzz"),
        (60, "fizzbuzz"),
        (65, "buzz"),
        (90, "fizzbuzz"),
        (93, "fizz"),
    ],
)
def test_fizz_buzz(number: int, expected: str):
    """Test."""
    result = fizz_buzz()
    assert result[number - 1] == expected


def test_fizz_buzz_returns_100_numbers():
    """Test."""
    result = generate_fizz_buzz_string().split("\n")
    assert len(result) == 100
