# https://www.hackerrank.com/challenges/repeated-string/problem

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    if 'a' not in s:
        return 0

    if len(s) == 1:
        return n

    a_list = []
    current_a_cnt = 0
    for c in s:
        if c == 'a':
            current_a_cnt += 1
        a_list.append(current_a_cnt)

    result = a_list[-1] * (n // len(s))
    if (n % len(s)) != 0:
        result += a_list[(n % len(s)) - 1]

    return result


print(repeatedString('x', 970770))
