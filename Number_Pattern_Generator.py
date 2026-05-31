def number_pattern(n):
    # Check if input is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Check if integer is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Initialize an empty string to build the result
    result = ""

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Add current number to the result string
        result += str(i)

        # Add a space after each number except the last one
        if i != n:
            result += " "

    # Return the final formatted string
    return result
