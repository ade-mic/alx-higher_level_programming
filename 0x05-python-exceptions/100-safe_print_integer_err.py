#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print('{:d}'.format(value), end='\n')
        return True
    except ValueError as err:
        print('Exception: ', err, file=sys.stderr)
    except TypeError as err:
        print('Exception: ', err, file=sys.stderr)
        return False
