def clean_list(data):
    # Remove duplicates manually
    unique_items = []
    for item in data:
        if item not in unique_items:
            unique_items.append(item)
    
    # Sort using a basic sorting algorithm (inefficient)
    for i in range(len(unique_items)):
        for j in range(i + 1, len(unique_items)):
            if unique_items[i] > unique_items[j]:
                temp = unique_items[i]
                unique_items[i] = unique_items[j]
                unique_items[j] = temp

    return unique_items

# Example
data = [5, 3, 1, 2, 3, 5, 4, 1]
print(clean_list(data))  # Output: [1, 2, 3, 4, 5]
