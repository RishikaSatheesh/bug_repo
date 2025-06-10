```python
def divide_vals(a,b,c):
    if b == 0 or c == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    print(divide_vals(10,5))
except ValueError as e:
    print(e)
```