n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], -x[0]))

result = 0
cur_time = 0
min_value = 1e9

for p, t in arr:
    if cur_time < t:
        cur_time += 1
        result += p
        min_value = min(min_value, p)
    elif min_value < p and cur_time - 1 < t:
        result -= min_value
        result += p
        min_value = p

print(result)