# O(nlogn) -- Worst O(n^2)
def quick_sort(values: list) -> list:
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    pivot = values[mid]

    left = [x for x in values if x < pivot]
    mid = [x for x in values if x == pivot]
    right = [x for x in values if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]

    print(quick_sort(test_1))
    print(quick_sort(test_2))
    print(quick_sort(test_3))


if __name__ == '__main__':
    main()
