n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

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
    prev = arr[0][i]
    for j in range(n):
        if prev == arr[j][i]:
            cnt += 1
        else:
            cnt = 1
        prev = arr[j][i]
    if cnt >= m:
        result += 1

print(result)