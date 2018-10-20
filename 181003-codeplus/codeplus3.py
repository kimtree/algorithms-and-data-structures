from itertools import product

width = 4
height = 4
chess = list(product(range(width), range(height)))


def route(start):
    stack = []
    visited = set()
    stack.append(start)

    max_depth = 0
    while stack:
        depth, start_pos = stack.pop(0)
        visited.add(start_pos)

        if max_depth < depth:
            max_depth = depth

        result_pos_set = set()
        for pos in [(2, -1), (2, 1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, -2), (-1, 2)]:
            result_pos = (start_pos[0] + pos[0], start_pos[1] + pos[1])
            if result_pos in chess and result_pos not in visited:
                result_pos_set.add(result_pos)

        for s in result_pos_set:
            pair = (depth+1, s)
            stack.append(pair)

    return max_depth, visited


max_depth, visited = route((0, chess[0]))
if set(visited) == set(chess):
    print("T", end='')
else:
    print("F", end='')

print(max_depth)