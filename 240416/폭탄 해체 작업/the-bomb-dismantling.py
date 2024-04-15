n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1])

result = 0
cur_time = 0

for p, t in arr:
    if cur_time < t:
        cur_time = t
        result += p

print(result)