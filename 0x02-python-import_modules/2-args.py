#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args = argv
    n_argv = len(args)

    if n_argv == 1:
        print('{} arguements.'.format(0))
    elif n_argv == 2:
        print('{} arguement:'.format(1))
        print('{}: {}'.format(1, args[1]))
    else:
        print('{} arguements:'.format(n_argv - 1))
        for i in range(1, n_argv):
            print('{}: {}'.format(i, args[i]))
