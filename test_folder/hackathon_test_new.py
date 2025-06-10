```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

safe_divide(10, 5)
```
Note: I replaced the duplicate input with an example value to test the function.