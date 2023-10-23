#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n_printed = 0
    for i in range(x):
        try:
            if (i < x - 1):
                print(my_list[i], end='')
            else:
                print(my_list[i], end='')
            n_printed += 1
        except IndexError:
            pass
    print('', end='\n')
    return n_printed
