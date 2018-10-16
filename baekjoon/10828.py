# BOJ 10828
import sys

stack = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline()
    if 'push' in command:
        stack.append(command.split()[1])
    elif 'top' in command:
        print(stack[-1] if stack else -1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        print('0' if stack else '1')
    elif 'pop' in command:
        print(stack.pop() if stack else -1)
