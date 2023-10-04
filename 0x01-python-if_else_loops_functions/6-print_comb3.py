#!/usr/bin/python3.8
for i in range(9):
    for j in range(1, 10):
        if i != (j + i) and (j + i < 10 ):
            if i < 8:
                print(f'{i}{j + i}', end=', ')
            else:
                print(f'{i}{i + j}', end='\n')
    