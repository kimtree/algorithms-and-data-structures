# O(nlogn)
def max_heapify(values: list, idx: int, size: int):
    new_idx = idx
    left_idx = idx * 2 + 1
    right_idx = idx * 2 + 2

    # Find max value from left, right child
    if left_idx < size and values[left_idx] >= values[new_idx]:
        new_idx = left_idx

    if right_idx < size and values[right_idx] >= values[new_idx]:
        new_idx = right_idx

    if new_idx != idx:
        values[new_idx], values[idx] = values[idx], values[new_idx]
        max_heapify(values, new_idx, size)


def heap_sort(values: list) -> list:
    # Build Max Heap
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(values, i, n)

    for i in range(n - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        max_heapify(values, 0, i)

    return values


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]
    test_4 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    print(heap_sort(test_1))
    print(heap_sort(test_2))
    print(heap_sort(test_3))
    print(heap_sort(test_4))


if __name__ == '__main__':
    main()
