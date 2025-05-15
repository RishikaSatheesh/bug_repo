```python
import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def load_data(self):
        try:
            self.data = pd.read_csv('data.csv')
        except FileNotFoundError:
            print("File not found. Please check the file path.")
            return False
        except pd.errors.EmptyDataError:
            print("No data in file. Please check the file content.")
            return False
        return True

    def process_data(self):
        # Remove duplicates using set()
        self.data = list(set(self.data))

        # Sort data in ascending order
        self.data.sort()

        return self.data


if __name__ == "__main__":
    data = []
    if DataProcessor(data).load_data():
        result = DataProcessor(data).process_data()
        print(result)
```