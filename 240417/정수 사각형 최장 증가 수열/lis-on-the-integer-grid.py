n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 0

cells = []
for i in range(n):
    for j in range(n):
        cells.append((arr[i][j], i, j))

cells.sort()

for _, i, j in cells:
    cur = arr[i][j]

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > cur:
            dp[nx][ny] = max(dp[nx][ny], dp[i][j] + 1)

for i in range(n):
    for j in range(n):
        result = max(result, dp[i][j])

print(result)