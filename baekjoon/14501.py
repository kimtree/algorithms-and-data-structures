# BOJ 14501
import sys
from collections import deque

job_count = int(sys.stdin.readline())

job_list = []
for _ in range(job_count):
    job_str = sys.stdin.readline().strip().split()
    job_list.append((int(job_str[0]), int(job_str[1])))

profit_list = []
for start_day in range(job_count):
    max_profit = 0

    stack = deque([(0, start_day)])
    while stack:
        profit, day = stack.popleft()
        if day > (job_count-1):
            break

        next_start_day = day + job_list[day][0]
        if next_start_day <= job_count:
            next_profit = profit + job_list[day][1]
            if next_profit > max_profit:
                max_profit = next_profit

            for next_day in range(next_start_day, job_count):
                stack.append((next_profit, next_day))

        profit_list.append(max_profit)

print(max(profit_list))
