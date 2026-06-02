def binary_search(search_list, value):
    # Store the values visited during the search
    path_to_target = []

    # Initialize search boundaries
    low = 0
    high = len(search_list) - 1

    # Continue searching while the search space is valid
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2

        # Get the value at the middle index
        value_at_middle = search_list[mid]

        # Record the value checked
        path_to_target.append(value_at_middle)

        # Target found
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'

        # Search the right half
        elif value > value_at_middle:
            low = mid + 1

        # Search the left half
        else:
            high = mid - 1

    # Target not found
    return [], "Value not found"


# Test cases
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
