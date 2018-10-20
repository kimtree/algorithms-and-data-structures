digits = 4
maximum_digits = [9, 9, 9, 9]
initial_digits = [7, 7, 9, 3]
count = 3000

error = False
for idx, i in enumerate(initial_digits):
    if maximum_digits[idx] < i:
        error = True
        break


def count_recur(idx):
    if idx >= 0:
        if initial_digits[idx] > maximum_digits[idx]:
            initial_digits[idx] -= (maximum_digits[idx] + 1)
            if idx > 0:
                initial_digits[idx-1] += 1
                count_recur(idx-1)


if error:
    print(-1)
else:
    for _ in range(count):
        initial_digits[-1] += 1
        count_recur(digits-1)

    for _ in initial_digits:
        print(_, end='')
