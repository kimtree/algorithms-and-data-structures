def solution(A: list, B: list) -> int:
    upper = [float('-inf')] * len(A)
    local_max = float('-inf')
    for i in range(len(A)):
        if A[i] > local_max:
            local_max = A[i]
        upper[i] = local_max

    lower = [float('-inf')] * len(B)
    local_max = float('-inf')
    for i in range(len(B) - 1, -1, -1):
        if B[i] > local_max:
            local_max = B[i]
        lower[i] = local_max

    local_min = float('inf')
    for i in range(len(A)):
        local_min = min(local_min, max(upper[i], lower[i]))

    return local_min

if __name__ == "__main__":
    assert solution([3, 4, 6], [6, 5, 4]) == 5
    assert solution([1, 2, 1, 1, 1, 4], [1, 1, 1, 3, 1, 1, 1]) == 2
    assert solution([-5, -1, -3], [-5, 5, -2]) == -1