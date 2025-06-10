```python
def divide_values(a, b, c):
    """
    Divide value 'a' by the sum of values 'b' and 'c'.
    
    Args:
        a (float): The value to be divided.
        b (float): Value used for division.
        c (float): Value used for division.

    Returns:
        float: Division result of value 'a' by 'b+c'.

    Raises:
        TypeError: If inputs are not numbers or if division by zero occurs.
    """

    try:
        # Check if inputs are numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError("Input values must be numbers.")

        # Compute sum of 'b' and 'c'
        div_sum = b + c

        # Check for division by zero
        if div_sum == 0:
            raise ZeroDivisionError(f"Cannot divide by zero: {a}/{div_sum}")

        # Divide value 'a' by the computed sum
        result = a / div_sum

        return result
    
    except ZeroDivisionError as e:
        print(e)
    
    except Exception as e:
        print("An unexpected error occurred:", str(e))
```