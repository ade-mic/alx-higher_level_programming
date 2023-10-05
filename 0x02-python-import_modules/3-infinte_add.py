#!/usr/bin/python3
from sys import argv
n_args = len(argv)
sum = 0
if n_args <= 1:
    print('{}'.format(sum))
else:
    for i in range(1, n_args):
        sum += int(argv[i])
    print('{}'.format(sum))
