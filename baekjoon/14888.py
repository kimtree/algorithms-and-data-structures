# BOJ 14888
import sys
import itertools

count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operator_count = list(map(int, sys.stdin.readline().split()))

operators = []

for i, c in enumerate(operator_count):
    operators.extend([i+1 for x in range(c)])

max_num = -1000000001
min_num = 1000000001
for c in itertools.permutations(operators, len(numbers) - 1):
    result = numbers[0]
    idx = 1
    for op in c:
        if op == 1:
            result += numbers[idx]
        elif op == 2:
            result -= numbers[idx]
        elif op == 3:
            result *= numbers[idx]
        elif op == 4:
            result = int(result / numbers[idx])

        idx += 1

    if result < min_num:
        min_num = result
    if result > max_num:
        max_num = result

print(max_num)
print(min_num)