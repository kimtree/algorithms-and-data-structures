# BOJ 13458
import sys
import math

rooms = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
gamdok = list(map(int, sys.stdin.readline().split()))

total_gamdok = 0

for student_cnt in students:
    remain_cnt = student_cnt - gamdok[0]
    if remain_cnt > 0:
        total_gamdok += math.ceil(remain_cnt / gamdok[1])

print(total_gamdok + len(students))