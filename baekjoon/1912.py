# BOJ 1912
import sys

count = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
result = [0] * count
result[0] = numbers[0]

if count == 1:
    print(numbers[0])
else:
    for idx in range(1, count):
        result[idx] = max(result[idx-1] + numbers[idx], numbers[idx])

    print(result)
    print(max(result))