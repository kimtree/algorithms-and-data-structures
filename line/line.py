#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def get_fare(distance):
    if distance <= 40:
        return 720
    else:
        remain = distance - 40
        c = math.ceil(remain / 8)
        return 720 + (c * 80)

if __name__ == '__main__':
    split = sys.stdin.readline().strip().split(' ')
    money = 20000
    is_printed = False
    for token in split:
        distance = int(token)
        if distance > 178 or distance < 4:
            print(money)
            is_printed = True
            break
        fare = get_fare(distance)

        if money - fare < 0:
            print(money)
            is_printed = True
            break
        else:
            money -= fare

    if not is_printed:
        print(money)