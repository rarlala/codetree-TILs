n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[0], x[1]))

result = 0
cur_time = 0
left_time = 0

for p, t in arr:
    if cur_time < t:
        cur_time += 1
        left_time += 1 if t - cur_time - 1 > 0 else 0
        result += p
    elif cur_time - left_time < t:
        left_time -= cur_time - left_time
        cur_time += 1
        result += p

print(result)