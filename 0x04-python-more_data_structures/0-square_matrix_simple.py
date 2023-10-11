#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    result = [list(map(lambda x: x **2, vector)) for vector in new_matrix]
    return result
