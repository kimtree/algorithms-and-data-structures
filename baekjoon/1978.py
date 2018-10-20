# BOJ 1978
import sys

count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

max_num = max(numbers)

result = [True] * (max_num + 1)
for i in range(2, max_num + 1):
    if i * i > max_num:
        continue

    if result[i]:
        for j in range(i*2, max_num + 1, i):
            result[j] = False

count = 0
for n in numbers:
    if n > 1 and result[n]:
        count += 1

print(count)