#!/usr/bin/python3
"""Module for Pascal's triangle"""


def pascal_triangle(n):
    """
    Function to return Pascal's triangle as list of lists of integers

    Args:
        n (int): Height of the triangle

    Returns:
        list: list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for line in range(1, n):
        row = [1] * (line + 1)
        for i in range(1, line):
            row[i] = triangle[line - 1][i - 1] + triangle[line - 1][i]
        triangle.append(row)

    return triangle
