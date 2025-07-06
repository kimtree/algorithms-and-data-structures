from collections import Counter

def solution(A: str) -> int:
    c = Counter(A)

    odd_cnt = 0
    for char, count in c.items():
        if count % 2 == 1:
            odd_cnt += 1

    if odd_cnt == 0 or odd_cnt == 1:
        return 0

    return odd_cnt - 1

if __name__ == '__main__':
    assert solution('ervervige') == 2
    assert solution('aaabab') == 0
    assert solution('x') == 0