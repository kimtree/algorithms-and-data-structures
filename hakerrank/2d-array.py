#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = - sys.maxsize
    for j in range(0, len(arr)-2):
        for i in range(0, len(arr[j])-2):
            print(i, j)
            hourglass_sum = arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+1][i+1] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2]

            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    return max_sum


print(hourglassSum([[-1, -1, 0, -9, -2, -2],
                    [-2, -1, -6, -8, -2, -5],
                    [-1, -1, -1, -2, -3, -4],
                    [-1, -9, -2, -4, -4, -5],
                    [-7, -3, -3, -2, -9, -9],
                    [-1, -3, -1, -2, -4, -5]]))