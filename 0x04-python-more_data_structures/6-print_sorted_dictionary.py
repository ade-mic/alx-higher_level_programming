#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = sorted([x for x in a_dictionary.keys()])
    for i in res:
        print('{}: {}'.format(i, a_dictionary.get(i)))
