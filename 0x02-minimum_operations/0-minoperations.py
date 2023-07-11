#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to reach n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to reach n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed.

    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
