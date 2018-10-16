# BOJ 15953
import itertools

amount_1 = [500, 300, 200, 50, 30, 10]
count_1 = [1, 2, 3, 4, 5, 6]

amount_2 = [512, 256, 128, 64, 32]
count_2 = [1, 2, 4, 8, 16]


def get_amount(amount, count, grade):
    if grade == 0:
        return 0

    grade_list = list(itertools.accumulate(count))
    if grade > grade_list[-1]:
        return 0

    for idx, g in enumerate(grade_list):
        if grade <= g:
            return amount[idx] * 10000

    return 0


t = int(input())
for _ in range(t):
    assumption_str = input()
    assumption = assumption_str.split(" ")
    print(get_amount(amount_1, count_1, int(assumption[0])) + get_amount(amount_2, count_2, int(assumption[1])))
