

fact_dict = {0: 1, 1: 1}

def factorial(n):
    if n == 1 or n == 0:
        return 1

    if n not in fact_dict:
        fact_dict[n] = n * factorial(n-1)

    return fact_dict[n]


def get(num):
    threes = num // 3
    result = 0
    for i in range(threes + 1):
        # i = 0 1
        three = i
        remain = num - (three * 3)

        a = factorial(three + remain)
        b = factorial(three)
        c = factorial(remain)

        tmp = round(a / (b * c))

        result += tmp

    return result

for i in range(1, 100000000 // 1000):
    factorial(i * 10)

print(fact_dict)
print(get(100000))
