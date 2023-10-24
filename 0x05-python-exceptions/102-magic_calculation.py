#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except Exception:
            pass
        res = res + (a ** b) / i
    res = res + a + b
    return res


dis.dis(magic_calculation)
