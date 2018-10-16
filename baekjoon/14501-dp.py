# BOJ 14501
# Dynamic Programming ver.
import sys

job_count = int(sys.stdin.readline())
job_list = []
result = [0] * (job_count + 1)
for _ in range(job_count):
    job_str = tuple(map(int, sys.stdin.readline().strip().split()))
    job_list.append(job_str)

for day in range(job_count):
    time, price = job_list[day]
    next_day = day + time
    for idx in range(day + 1):
        if next_day <= job_count:
            result[next_day] = max(result[next_day], result[idx] + price)

print(max(result))
