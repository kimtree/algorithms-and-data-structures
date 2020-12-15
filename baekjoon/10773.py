# BOJ 10773
def main():
    count = int(input())

    numbers = []
    for i in range(count):
        i = int(input())
        if i == 0 and numbers:
            numbers.pop()
        if i != 0:
            numbers.append(i)

    print(sum(numbers))


if __name__ == '__main__':
    main()
