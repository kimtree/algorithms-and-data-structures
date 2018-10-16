# BOJ 1874
import sys

stack = []
n = int(sys.stdin.readline())
numbers = list(range(1, n+1))
numbers.reverse()
result_stack = []

is_closed = False

for _ in range(n):
    input = int(sys.stdin.readline().strip())

    top = stack[-1] if stack else -1
    if top == -1 or top < input:
        while True:
            top = stack[-1] if stack else -1
            if top != input:
                result_stack.append("+")
                stack.append(numbers.pop())
            elif top == input:
                stack.pop()
                result_stack.append("-")
                break
    elif top == input:
        stack.pop()
        result_stack.append("-")
    else:
        is_closed = True
        break

if is_closed:
    print("NO")
else:
    print("\n".join(result_stack))
