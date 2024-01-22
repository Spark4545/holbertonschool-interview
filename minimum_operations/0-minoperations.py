#!/usr/bin/python3
"""Summary
"""


def minOperations(n):
    """Function to determine the minimal number of operation to
    have n number of character in a file

    Args:
        n (int): number of character to have in the file
    """
    div = 2
    min_ops = 0

    while(isinstance(n, int) and n > 1):
        while(n % div):
            div += 1
        min_ops += div
        n = n // div
    return min_ops
