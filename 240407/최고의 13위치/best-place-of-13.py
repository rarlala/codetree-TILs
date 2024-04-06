n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = 0

for i in range(n):
    for j in range(n - 2):
        result = max(result, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(result)