```python
def divide_vals(a, b):
    """
    Divides a by b and returns the result.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.
    """
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def main():
    num1 = 10
    num2 = 5
    result = divide_vals(num1, num2)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
```