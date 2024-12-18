def linear_search(arr, target):
    """
    Perform a linear search to find the index of the target in the array.
    
    Parameters:
    arr (list): The list of elements to search.
    target (any): The element to find in the list.
    
    Returns:
    int: The index of the target if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage
numbers = [4, 2, 7, 1, 9, 3]
target = 7

result = linear_search(numbers, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
