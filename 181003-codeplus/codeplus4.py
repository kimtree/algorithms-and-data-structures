import itertools
numbers = [1, 2, 3, 4, 5]
answer = 8

result = set()

combinations = itertools.combinations(numbers, 3)
for c in combinations:
    if sum(c) == answer:
        result.add(c)

if not result:
    print("NO")
else:
    result = list(result)
    result.sort()

    for r in result:
        print(r[0], r[1], r[2])

