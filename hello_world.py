print("Hello world")


def sum_two_numbers(a, b):
    """
    Sum two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def sum_multiple_numbers(*args):
    """
    Sum multiple numbers passed as arguments.
    
    Args:
        *args: Variable number of arguments
    
    Returns:
        The sum of all arguments
    """
    return sum(args)


# Test the functions
if __name__ == "__main__":
    print(f"Sum of 5 and 10: {sum_two_numbers(5, 10)}")
    print(f"Sum of 1, 2, 3, 4, 5: {sum_multiple_numbers(1, 2, 3, 4, 5)}")
