# O(n^2)
def bubble_sort(values: list) -> list:
    for i in range(len(values) -1):
        for j in range(i, len(values)):
            if values[i] >= values[j]:
                values[i], values[j] = values[j], values[i]

    return values


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]

    print(bubble_sort(test_1))
    print(bubble_sort(test_2))
    print(bubble_sort(test_3))


if __name__ == '__main__':
    main()
