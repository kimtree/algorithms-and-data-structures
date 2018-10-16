# BOJ 14502
import sys
from collections import deque
from itertools import combinations


def count_safe_zone(laboratory, starting_points, wall_pos_list):
    for wall in wall_pos_list:
        laboratory[wall[0]][wall[1]] = 1

    remain = set(possible_wall_pos) - set(wall_pos_list)

    stack = deque()
    stack.extend(starting_points)
    next_params = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while stack:
        pos = stack.popleft()

        if not remain:
            break

        for p in next_params:
            result_pos = (pos[0] + p[0], pos[1] + p[1])
            if 0 <= result_pos[0] < height and 0 <= result_pos[1] < width:
                if result_pos in remain:
                    remain.remove(result_pos)
                    stack.append(result_pos)

    return len(remain)


size_str = sys.stdin.readline().strip().split()
height = int(size_str[0])
width = int(size_str[1])

possible_wall_pos = []
starting_points = []
laboratory_map = []
for _ in range(height):
    map_str = sys.stdin.readline().strip().split()
    map_str = [int(x) for x in map_str]
    for idx, c in enumerate(map_str):
        if c == 0:
            possible_wall_pos.append((_, idx))
        elif c == 2:
            starting_points.append((_, idx))
    laboratory_map.append(map_str)

remain_count = len(possible_wall_pos)
max = 0
for c in combinations(possible_wall_pos, 3):
    count = count_safe_zone([row[:] for row in laboratory_map], starting_points, c)
    if count > max:
        max = count

print(max)