# BOJ 2606
def main():
    _ = int(input())
    nodes = int(input())

    node_map = {}
    for i in range(nodes):
        route = input().strip()
        data = route.split()
        if data[0] not in node_map:
            node_map[data[0]] = [data[1]]
        else:
            node_map[data[0]].append(data[1])

        if data[1] not in node_map:
            node_map[data[1]] = [data[0]]
        else:
            node_map[data[1]].append(data[0])

    visited = set()
    queue = ['1']
    while queue:
        start = queue.pop(0)
        if start not in visited:
            visited.add(start)

            if start in node_map:
                for n in node_map[start]:
                    if n not in visited:
                        queue.append(n)

    print(len(visited) - 1)


if __name__ == '__main__':
    main()
