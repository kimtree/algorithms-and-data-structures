# O(nlogn) / use more spaces
def merge_sort(values: list) -> list:
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    left_list = values[:mid]
    right_list = values[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    i = j = 0
    result = []

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1

    result += left_list[i:]
    result += right_list[j:]

    return result


def main():
    test_1 = [1, 2, 3, 4, 5]
    test_2 = [5, 4, 3, 2, 1]
    test_3 = [1, 5, 3, 9, 7]

    print(merge_sort(test_1))
    print(merge_sort(test_2))
    print(merge_sort(test_3))


if __name__ == '__main__':
    main()
