# BOJ 1912
import sys

count = int(sys.stdin.readline())
result = [0] * (count+1)

numbers = list(map(int, sys.stdin.readline().split()))

for i, number in enumerate(numbers):
    for idx in range(i, count):
        if result[i] < result[i] + numbers[idx]:
            result[i] += numbers[idx]
        else:
            break

print(max(result))