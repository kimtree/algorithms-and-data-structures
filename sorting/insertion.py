# O(n^2)
def insertion_sort(values: list) -> list:
    for i in range(1, len(values)):
        idx = i - 1
        key = values[i]
        while idx >= 0 and values[idx] > key:
            values[idx], values[idx+1] = values[idx+1], values[idx]
            idx -= 1

        values[idx+1] = key

    return values


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]

    print(insertion_sort(test_1))
    print(insertion_sort(test_2))
    print(insertion_sort(test_3))


if __name__ == '__main__':
    main()
