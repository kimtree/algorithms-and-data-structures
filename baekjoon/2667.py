# BOJ 2667
import sys
import collections

map_size = int(sys.stdin.readline())

apt_map = []
for i in range(map_size):
    tmp_map = [x for x in sys.stdin.readline().strip()]
    apt_map.append(tmp_map)

stack = collections.deque()

visited = set()
res_list = []

for i in range(map_size):
    for j in range(map_size):
        if apt_map[i][j] == '1' and (i, j) not in visited:
            stack.append((i, j))

        res_cnt = 0
        while stack:
            (x, y) = stack.popleft()
            if (x, y) not in visited:
                res_cnt += 1
                visited.add((x, y))

                for res_x, res_y in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if 0 <= res_x < map_size and 0 <= res_y < map_size:
                        if apt_map[res_x][res_y] == '1' and (res_x, res_y) not in visited:
                            stack.append((res_x, res_y))

        if res_cnt != 0:
            res_list.append(res_cnt)

print(len(res_list))
res_list.sort()
for v in res_list:
    print(v)