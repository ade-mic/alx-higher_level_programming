#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print('{:d}'.format(value), end='\n')
        return True
    except (ValueError, TypeError) as err:
        print('Exception: ', err, file=sys.stderr)
