# BOJ 15686
import sys
import itertools

map_info = list(map(int, sys.stdin.readline().split()))
size = map_info[0]
chicken_count = map_info[1]

town_map = []
for _ in range(size):
    map_info = sys.stdin.readline().split()
    town_map.append(map_info)

houses = set()
chicken_store = set()
for i in range(size):
    for j in range(size):
        if town_map[i][j] == '1':
            houses.add((i, j))
        elif town_map[i][j] == '2':
            chicken_store.add((i, j))

distance_list = []
for c in itertools.combinations(chicken_store, chicken_count):
    total_dis = 0
    for h_x, h_y in houses:
        min_dis = 9999999
        for c_x, c_y in c:
            dis = abs(c_x - h_x) + abs(c_y - h_y)
            if dis < min_dis:
                min_dis = dis

        total_dis += min_dis

    distance_list.append(total_dis)

print(min(distance_list))
