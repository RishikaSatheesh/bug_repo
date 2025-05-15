```python
import logging

# Set up logging configuration
logging.basicConfig(filename='log.txt', level=logging.INFO)

def print_greeting(num_spaces):
    """Prints a decorated greeting message."""
    greeting = 'Hello World!' + ' ' * num_spaces
    print(greeting)

def read_and_process_file(file_path, chunk_size=1024):
    """
    Reads the file in chunks and processes it.

    Args:
        file_path (str): Path to the file.
        chunk_size (int, optional): Size of each chunk. Defaults to 1024.

    Returns:
        None
    """
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                # Process the chunk here...
                logging.info(f"Processed {len(chunk)} bytes")
    except FileNotFoundError:
        logging.error("File not found")

def main():
    event_name = "hackathon"
    print_greeting(4)  # Number of spaces for decoration
    
    file_path = "example.txt"  # Replace with your actual file path
    read_and_process_file(file_path)

if __name__ == "__main__":
    main()
```