#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists of integers.

    Args:
        n (int): the number of rows. Returns [] if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
