def selection_sort(items):
    n = len(items)

    # Traverse through all elements
    for i in range(n):

        # Assume current position is the minimum
        min_index = i

        # Find the actual minimum in remaining unsorted part
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j

        # Swap only if a smaller element was found
        if min_index != i:
            temp = items[i]
            items[i] = items[min_index]
            items[min_index] = temp

    return items
