# BOJ 2178
import sys


def find_exit(miro):
    stack = [(0, 0, 0)]
    visited = []

    max_depth = 0
    while stack:
        (x, y, depth) = stack.pop(0)

        if max_depth < depth:
            max_depth = depth

        if x == height-1 and y == width-1:
            return depth+1

        if (x, y) not in visited:
            visited.append((x, y))

            for path in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                result_pos = (x + path[0], y + path[1])
                if 0 <= result_pos[0] < height and 0 <= result_pos[1] < width:
                    if miro[result_pos[0]][result_pos[1]] == '1':
                        stack.append((result_pos[0], result_pos[1], depth+1))

    return max_depth


tmp = sys.stdin.readline().split()
height = int(tmp[0])
width = int(tmp[1])

miro = []
for h in range(height):
    line = []
    edge_str = sys.stdin.readline().strip()
    for x, e in enumerate(edge_str):
        line.append(e)
    miro.append(line)

print(find_exit(miro))
