#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Args:
        matrix(list of lists of integers/floats)
        div(int or float)
    """
    message_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    message_2 = 'Each row of the matrix must have the same size'
    message_3 = 'div must be a number'
    message_4 = 'division by zero'
    if not isinstance(matrix, list):
        raise TypeError(message_1)
    if not isinstance(matrix[0], list):
        raise TypeError(message_1)
    if not isinstance(div, (int, float)):
        raise TypeError(message_3)
    if div == 0:
        raise ZeroDivisionError(message_4)
    # lenght for the first row
    len_row = len(matrix[0])
    # instantiate new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        # check size of row
        if len(row) < len_row:
            raise TypeError(message_2)
        for i in row:
            # check list of list contains only int or float
            if (not isinstance(i, (int, float))):
                raise TypeError(message_1)
            # append each element
            new_row.append(round(i / div, 2))
        # append the each row to new_matrix
        new_matrix.append(new_row)
    # return new_matrix
    return new_matrix
