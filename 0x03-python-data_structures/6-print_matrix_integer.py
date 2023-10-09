#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        for i in range(len(vector)):
            if i < len(vector) - 1:
                print('{:d}'.format(vector[i]), end=' ')
            else:
                print('{:d}'.format(vector[i]), end='\n')
