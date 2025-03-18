from typing import Callable
import re

def generator_numbers(text: str):
    """
    Generates real numbers from a given string.

    Parameters:
    ----------
    text : str
        The string from which to extract real numbers.

    Yields:
    -------
    float
        The next real number as a float.

    Example usage:
    ---------------------
    >>> numbers = generator_numbers("These numeric values: -1.5, 2.0, 3.14159")
    >>> list(numbers)
    [-1.5, 2.0, 3.14159]
    """
    # Regular expression for real numbers
    pattern = r'-?\d+\.?\d*|-?\.\d+'
    # https://www.geeksforgeeks.org/re-finditer-in-python/
    matches = re.finditer(pattern, text)

    for match in matches:
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    """
    Calculate the total profit from a given text by applying a specified function.

    Parameters:
    ----------
    text : str
        The input string containing numeric values from which to calculate profit.
        
    func : Callable
        A function that processes the input text and returns an iterable of numeric values.

    Returns:
    -------
    float
        The total profit calculated by summing the numeric values obtained from the input text.

    Example:
    --------
    >>> def extract_numbers(s: str):
    ...     # Example function that extracts numbers from a string
    ...     return [float(num) for num in s.split() if num.isdigit()]
    >>> total_profit = sum_profit("The profits are 100 200 300", extract_numbers)
    >>> print(total_profit)
    600.0
    """
    # https://www.geeksforgeeks.org/sum-function-python/
    total = sum(func(text))
    return total


if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    gen = generator_numbers(text)
    assert next(gen) == 1000.01
    assert next(gen) == 27.45
    assert next(gen) == 324.0

    assert sum_profit(text, generator_numbers) == 1351.46

    # total_income = sum_profit(text, generator_numbers)
    # print(f"Загальний дохід: {total_income}")
