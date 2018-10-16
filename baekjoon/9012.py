# BOJ 9012
import sys


def detect_parenthesis(input_str):
    stack = []
    for i in input_str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack):
        return False
    else:
        return True


result = []
n = int(sys.stdin.readline())
for _ in range(n):
    input_str = sys.stdin.readline().strip()
    result.append("YES" if detect_parenthesis(input_str) else "NO")

print("\n".join(result))