```python
def divide_val(a, b):
    """
    Divide two numbers and return the result.
    
    Parameters:
        a (float): The dividend.
        b (float): The divisor.
    
    Returns:
        float: The division result.
    
    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None

# Example usage:
result = divide_val(10, 5)
if result is not None:
    print(result)
```