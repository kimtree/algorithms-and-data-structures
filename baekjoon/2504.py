# BOJ 2504
import sys

is_failed = False
input_str = sys.stdin.readline().strip()
score = 0
stack = []

tmp_score = 1
for i in input_str:
    if i == '(':
        stack.append(i)
        tmp_score *= 2
    elif i == '[':
        stack.append(i)
        tmp_score *= 3
    elif i == ')'or i == ']':
        if len(stack) == 0:
            is_failed = True
            break
        else:
            top = stack[-1] if stack else -1
            if (i == ')' and top == '(') or (i == ']' and top == '['):
                stack.pop()
                score += tmp_score
            if i == ')':
                tmp_score /= 2
            elif i == ']':
                tmp_score /= 3

if len(stack) == 0:
    print(score)
else:
    print(0)
