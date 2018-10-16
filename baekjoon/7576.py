# BOJ 7576
import sys
from collections import deque

input_str = sys.stdin.readline().strip().split()
width = int(input_str[0])
height = int(input_str[1])

tomato = []
for _ in range(height):
    tomato_line = sys.stdin.readline().strip().split()
    tomato.append(tomato_line)

to_ripe = 0
stack = deque()
days = 0

for x, line in enumerate(tomato):
    for y, t in enumerate(line):
        if tomato[x][y] == '1':
            stack.append((days, (x, y)))
        elif tomato[x][y] == '0':
            to_ripe += 1

if to_ripe == 0:
    print(0)
else:
    visited = {}

    while stack:
        days, pos = stack.popleft()

        if tomato[pos[0]][pos[1]] == '0':
            to_ripe -= 1

        if to_ripe == 0:
            break

        next_params = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for p in next_params:
            result_pos = (pos[0] + p[0], pos[1] + p[1])
            if 0 <= result_pos[0] < height and 0 <= result_pos[1] < width:
                if tomato[result_pos[0]][result_pos[1]] != '-1' and result_pos not in visited:
                    visited[result_pos] = 1
                    stack.append((days+1, result_pos))

    if to_ripe == 0:
        print(days)
    else:
        print(-1)
