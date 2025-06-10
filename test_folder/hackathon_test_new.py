```
def divide_vals(a):
    try:
        return a/0
    except ZeroDivisionError:
        print("Error! Division by zero is undefined.")
        return None

result = divide_vals(10)
if result is not None:
    print(result)
else:
    print("Function returned an error.")

```