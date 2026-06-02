def square_root_bisection(square_target, tolerance=1e-7, maximum_iterations=100):

    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)

    iterations = 0

    while (high - low) > tolerance and iterations < maximum_iterations:
        midpoint = (low + high) / 2

        if midpoint * midpoint < square_target:
            low = midpoint
        else:
            high = midpoint

        iterations += 1

    if (high - low) <= tolerance:
        root = (low + high) / 2
        print(f"The square root of {square_target} is approximately {root}")
        return root

    print(f"Failed to converge within {maximum_iterations} iterations")
    return None
