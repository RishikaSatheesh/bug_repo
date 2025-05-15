```python
def multiply_values(a, b):
    """
    This function multiplies two input values and returns their product.
    
    Args:
        a (float): The first value to be multiplied.
        b (float): The second value to be multiplied.
        
    Returns:
        float: The product of the input values.
        
    Raises:
        TypeError: If either of the inputs is not a number.
        ValueError: If either of the inputs is zero.
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers")
        if a == 0 or b == 0:
            raise ValueError("Neither input can be zero.")
        
        return a * b
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```