# BOJ 1697
import sys
from collections import deque

input_str = sys.stdin.readline().strip().split()
current_pos = int(input_str[0])
destination_pos = int(input_str[1])

if current_pos >= destination_pos:
    print(current_pos - destination_pos)
else:
    stack = deque()
    stack.append((0, current_pos))
    visited = {}

    while stack:
        time, pos = stack.popleft()

        if pos == destination_pos:
            print(time)
            break

        if pos not in visited:
            visited[pos] = 1

            next_pos_candidates = [pos - 1]
            if pos < destination_pos:
                next_pos_candidates.extend([pos + 1, pos * 2])

            next_pos_list = []
            for c in next_pos_candidates:
                if 0 <= c <= 100000 and c not in visited:
                    next_pos_list.append((time + 1, c))

            stack.extend(next_pos_list)
