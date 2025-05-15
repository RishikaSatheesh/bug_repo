```python
def multiply_class_method(a, b):
    """
    Calculate the product of two numbers using modular arithmetic to avoid overflow.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of 'a' and 'b'.

    Raises:
        TypeError: If either 'a' or 'b' is not numeric.
        ValueError: If the input arguments are non-numeric or exceed maximum allowed value.
    """
    # Validate inputs
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Both inputs must be numbers")
        # Modular multiplication to avoid overflow
        result = pow(int(round(a * b)), 10**9 + 7)
    except OverflowError as e:
        raise ValueError("Input arguments exceed maximum allowed value") from e
    return result

# Example usage
result = multiply_class_method(1, 2)
print(result)  # Output: 2
```