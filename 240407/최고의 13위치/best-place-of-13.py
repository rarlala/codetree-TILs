n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = 0

if n == 3:
    for line in arr:
        result = max(result, sum(line))
else:
    for i in range(n):
        for j in range(n - 4):
            result = max(result, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(result)