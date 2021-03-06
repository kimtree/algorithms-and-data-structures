# BOJ 1260
import sys
import collections

tmp = sys.stdin.readline().split()


def dfs(graph, start):
    stack = collections.deque()
    stack.appendleft(start)
    visited = []

    while stack:
        node = stack.popleft()
        if node not in visited:
            visited.append(node)

            if node in graph:
                children_node = list(set(graph[node]) - set(visited))
                children_node.sort()

                stack.extendleft(reversed(children_node))

    return visited


def bfs(graph, start):
    stack = collections.deque()
    stack.appendleft(start)
    visited = []

    while stack:
        node = stack.popleft()
        if node not in visited:
            visited.append(node)

            if node in graph:
                children_node = list(set(graph[node]) - set(visited))
                children_node.sort()

                stack.extend(children_node)

    return visited


graph = {}
for _ in range(int(tmp[1])):
    edge_str = sys.stdin.readline().split()

    edge_from = int(edge_str[0])
    edge_to = int(edge_str[1])

    if edge_from not in graph:
        graph[edge_from] = [edge_to]
    else:
        graph[edge_from].append(edge_to)
        graph[edge_from].sort()

    if edge_to not in graph:
        graph[edge_to] = [edge_from]
    else:
        graph[edge_to].append(edge_from)
        graph[edge_to].sort()


path = dfs(graph, int(tmp[2]))
for p in path:
    print(p, end=' ')

path = bfs(graph, int(tmp[2]))
print()
for p in path:
    print(p, end=' ')
