# BOJ 15685
import sys

positions = set()


def draw_dragon_curves(x, y, d, g):
    positions.add((x, y))
    directions = [d]

    for i in range(1, g+1):
        for v in reversed(directions):
            directions.append((v+1) % 4)

    for direction in directions:
        new_x, new_y = get_next_position(x, y, direction)
        positions.add((new_x, new_y))
        x, y = new_x, new_y


def get_next_position(x, y, dir):
    if dir == 0:
        return x+1, y
    elif dir == 1:
        return x, y-1
    elif dir == 2:
        return x-1, y
    elif dir == 3:
        return x, y+1


size_of_curves = int(sys.stdin.readline())
for _ in range(size_of_curves):
    start_x, start_y, d, g = sys.stdin.readline().strip().split()
    draw_dragon_curves(int(start_x), int(start_y), int(d), int(g))

rect = 0
for x, y in positions:
    if (x+1, y) in positions and (x, y+1) in positions and (x+1, y+1) in positions:
        rect += 1

print(rect)