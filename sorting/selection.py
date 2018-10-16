# O(n^2)
def selection_sort(values: list) -> list:
    result_idx = -1
    for i in range(len(values) - 1):
        for j in range(i, len(values)):
            if values[i] >= values[j]:
                result_idx = j

        if result_idx != -1:
            values[i], values[result_idx] = values[result_idx], values[i]

    return values


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]

    print(selection_sort(test_1))
    print(selection_sort(test_2))
    print(selection_sort(test_3))


if __name__ == '__main__':
    main()
