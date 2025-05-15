```python
import os

def load_data(file_path):
    """
    Load data from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        list: Loaded data.
    """
    try:
        with open(file_path, 'r') as f:
            data = [line.strip() for line in f]
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

def process_data(data):
    """
    Process the loaded data.

    Args:
        data (list): Loaded data.

    Returns:
        list: Processed data.
    """
    try:
        # Use a more efficient approach to process the data
        processed_data = [line.strip() for line in data]
        return processed_data
    except Exception as e:
        print(f"Error processing data: {e}")
        return []

def save_data(file_path, data):
    """
    Save data to a file.

    Args:
        file_path (str): Path to the file.
        data (list): Data to be saved.
    """
    try:
        with open(file_path, 'w') as f:
            for line in data:
                f.write(line + "\n")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    file_path = "data.txt"
    data = load_data(file_path)
    processed_data = process_data(data)
    save_data("processed_data.txt", processed_data)

if __name__ == "__main__":
    main()
```