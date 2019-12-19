# BOJ 11403
import sys
import collections

size = int(sys.stdin.readline())

graph = {}
for i in range(size):
    graph[i] = []

for i in range(size):
    line = map(int, sys.stdin.readline().split())
    for idx, j in enumerate(line):
        if j == 1:
            graph[i].append(idx)

result = []
for i in range(size):
    result.append([0 for x in range(size)])


def bfs():
    for i in range(size):
        stack = collections.deque()
        stack.appendleft(i)

        while stack:
            n = stack.popleft()
            for node in graph[n]:
                if result[i][node] == 0:
                    result[i][node] = 1
                    stack.append(node)


bfs()
for f in result:
    for t in f:
        print(t, end=' ')
    print()
