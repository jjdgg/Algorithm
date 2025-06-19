n = int(input())
times = list(map(int, input().split()))
times.sort()

accu_time = 0
total_time = 0

for t in times:
    accu_time += t
    total_time += accu_time

print(total_time)