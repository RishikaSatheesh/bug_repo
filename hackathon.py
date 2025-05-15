```python
#!/usr/bin/env python

"""
This module contains functions for solving problems related to data structures.
"""

import typing as t

def calculate_sum(numbers: t.List[int]) -> int:
    """
    Calculate the sum of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the numbers in the list.

    Raises:
        ValueError: If the input is not a list or if the list contains non-integer values.
    """
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list")
    try:
        return sum(numbers)
    except TypeError:
        raise ValueError("List must contain only integers")


def main():
    # Example usage
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(result)  # Output: 15


if __name__ == "__main__":
    main()
```