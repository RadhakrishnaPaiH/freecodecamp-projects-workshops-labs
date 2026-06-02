def quick_sort(integers):
    # Base case: a list with 0 or 1 element is already sorted
    if len(integers) <= 1:
        return integers[:]

    # Choose the last element as the pivot
    pivot_value = integers[-1]

    # Create lists to store values less than,
    # equal to, and greater than the pivot
    left = []
    middle = []
    right = []

    # Partition the input list based on the pivot value
    for item in integers:
        if item < pivot_value:
            left.append(item)
        elif item == pivot_value:
            middle.append(item)
        else:
            right.append(item)

    # Recursively sort the left and right partitions,
    # then combine them with the pivot values in the middle
    return quick_sort(left) + middle + quick_sort(right)
