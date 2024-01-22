#!/usr/bin/env python3
"""Summary
"""


def minOperations(n):
    """summary
    """
    div = 2
    min_ops = 0

    while(isinstance(n, int) and n > 1):
        while(n % div):
            div += 1
        min_ops += div
        n = n // div
    return min_ops
