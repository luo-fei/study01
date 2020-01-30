#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math


def multi_isinstance ( a, b, c ) :
    z = [False for i in (a, b, c) if not isinstance ( i, (int))]
    if z :
        return False
    else :
        return True


def quadratic(a, b, c):
    if not multi_isinstance(a, b, c):
          raise TypeError(' Bad operand type')

    if a == 0:
        x1 = -(c / b)
        x2 = x1
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic(2, 5, 3))
