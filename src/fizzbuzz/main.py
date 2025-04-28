"""Main module for the FizzBuzz kata.

# Requirements

1. Create a method that prints out the numbers 1 through 100, separated by newlines.
2. Instead of numbers divisible by 3, the method should output "Fizz".
3. Instead of numbers divisible by 5, the method should output "Buzz".
4. Instead of numbers divisible by 3 and 5, the method should output "FizzBuzz".

# Extra requirements

- Instead of numbers with a three in them, print "Fizz".
- Instead of numbers with a five in them, print "Buzz".
- Instead of numbers with a three and a five in them, print "FizzBuzz".
"""


def hello_world() -> str:
    """Entrypoint for FizzBuzz."""
    return "Hello world!"

def _single_fizz_buzz(number: int) -> str:
    if number % 3 == 0:
        return "fizz"

    return str(number)

def fizz_buzz() -> list[str]:
    result = []
    for number in range(1, 100):
        result.append(_single_fizz_buzz(number))

    return result


def generate_fizz_buzz_string() -> str:
    result = ""
    for number in fizz_buzz():
        result += number + "\n"

    return result


def app() -> None:  # pragma: no cover
    """Entrypoint for FizzBuzz."""
    print(hello_world())


if __name__ == "__main__":  # pragma: no cover
    app()
