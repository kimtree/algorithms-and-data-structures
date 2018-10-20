import itertools


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True


def find_pos(orig_str, s):
    s = list(s)
    init_pos = last_pos = -1
    for idx, x in enumerate(orig_str):
        if x == s[-1]:
            if init_pos == -1:
                init_pos = idx
            s.pop()
            if len(s) == 0:
                last_pos = idx
                break

    return (init_pos, last_pos)


def has_not_overlap(orig_str, s1, s2):
    s1_pos = find_pos(orig_str, s1)
    s2_pos = find_pos(orig_str, s2)

    check1 = check2 = False
    if s1_pos[1] != -1 and s2_pos[0] != -1 and s1_pos[1] < s2_pos[0]:
        check1 = True

    if s2_pos[1] != -1 and s1_pos[0] != -1 and s2_pos[1] < s1_pos[0]:
        check2 = True

    return (check1 or check2)


def getScore(s):
    score = -9999
    char_list = [x for x in s]
    pal_set = set()
    for x in s:
        pal_set.add(x)

    for l in range(2, len(s)):
        comb = itertools.combinations(char_list, l)
        for c in comb:
            if is_palindrome(c):
                pal_set.add(c)

    for c in itertools.combinations(pal_set, 2):
        left, right = c[0], c[1]
        if has_not_overlap(s, left, right):
            print(left, right)
            result = len(left) * len(right)
            if result > score:
                score = result

    return score

print(getScore('acdapmpomp'))
#print(find_pos('acdapmpomp', 'aca'))