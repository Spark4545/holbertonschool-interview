#!/usr/bin/python3
"""Module which contains minoperations function"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
        to result in exactly n H characters in the file

        Args:
            n: repetitions of H

        Returns:
            number of operations (Copy & Paste) to reach n Hs
    """
    div = 2
    min_ops = 0

    while(isinstance(n, int) and n > 1):
        while(n % div):
            div += 1
        min_ops += div
        n = n // div
    return min_ops
