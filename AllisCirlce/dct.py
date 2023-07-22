def add(a, b):
    """
    Add two numbers and returns the sum.

    Example:
    >>> add(3, 4)
    7
    >>> add(8, 10)
    18
    >>> add(-1, 1)
    0
    """

    return a + b

def subtract(a, b):
    """
    Substract two numbers and return the result.

    Examples:
    >>> subtract(10, 5)
    5
    >>> subtract(3, 7)
    -4
    """
    return a - b



if __name__ == '__main__':
    import doctest
    doctest.testmod()
