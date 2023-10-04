#!/usr/bin/python3
def fizzbuzz():
    out = ''
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            out = out + 'FizzBuzz '
        elif i % 3 == 0:
            out = out + 'Fizz '
        elif i % 5 == 0:
            out = out + 'Buzz '
        else:
            out = out + f'{i} '
    print(out)
