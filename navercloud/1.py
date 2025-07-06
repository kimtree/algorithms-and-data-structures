def solution(numbers: list) -> int:
    N = len(numbers)


    left = [float('-inf')] * N
    local_max = float('-inf')
    for i in range(2, N):
        if local_max < numbers[i-2]:
            local_max = max(local_max, numbers[i-2])
            left[i] = numbers[i-2]
        else:
            left[i] = local_max

    right = [float('-inf')] * N
    local_max = float('-inf')
    for i in range(N - 3, -1, -1):
        if local_max < numbers[i+2]:
            local_max = max(local_max, numbers[i+2])
            right[i] = numbers[i+2]
        else:
            right[i] = local_max

    print(left)
    print(right)

    local_max = float('-inf')
    for i in range(2, N-2):
        s = left[i] + numbers[i] + right[i]
        if s > local_max:
            local_max = s

    return local_max

if __name__ == "__main__":
    assert solution([8, -4, -7, -5, -5, -4, 8, 8]) == 12
    assert solution([-2, -8, 1, 5, -8, 4, 7, 6]) == 15
    assert solution([-3, 0, -6, -7, -9, -5, -2, -6]) == -9
    assert solution([-10, -10, -10, -10, -10]) == -30