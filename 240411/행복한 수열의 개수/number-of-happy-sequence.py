n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = list(map(list, zip(*arr)))

result = 0
for i in range(n):
    cnt = 1
    prev = arr[i][0]
    for j in arr[i]:
        if prev == j:
            cnt += 1
        else:
            cnt = 1
        prev = j
    if cnt >= m:
        result += 1

for i in range(n):
    cnt = 1
    prev = new_arr[i][0]
    for j in new_arr[i]:
        if prev == j:
            cnt += 1
        else:
            cnt = 1
        prev = j
    if cnt >= m:
        result += 1

print(result)