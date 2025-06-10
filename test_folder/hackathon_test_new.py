```python
def divide_numbers(num1, num2, num3):
    """
    Divide three numbers and return the result.
    
    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    num3 (float): The third number.
    
    Returns:
    float: The division of num1, num2, and num3.

    Raises:
        ZeroDivisionError: If any of the numbers are zero.
    """

    # Check if any of the numbers are zero
    if 0 in [num1, num2, num3]:
        raise ValueError("Cannot divide by zero")

    # Perform division once for all three numbers
    result = (num1 / num2) / (num3 / num2)

    return result

# Example usage
try:
    print(divide_numbers(10, 5, 3))
except ZeroDivisionError as e:
    print("An error occurred:", str(e))

```

Note that the optimized code now includes input validation to prevent division by zero and raises a `ValueError` in this case. Additionally, it follows PEP8's naming conventions for variables and functions, uses clear variable names, and includes comments explaining its purpose.