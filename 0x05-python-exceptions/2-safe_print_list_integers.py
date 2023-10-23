#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            n_printed += 1
        except (ValueError, TypeError):
            pass
    print('', end='\n')
    return n_printed
