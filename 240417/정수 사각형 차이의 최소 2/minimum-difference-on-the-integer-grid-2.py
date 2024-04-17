n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[(100, 1)] * n for _ in range(n)]

dp[0][0] = (arr[0][0], arr[0][0])

for i in range(1, n):
    min_v = min(arr[i][0], dp[i - 1][0][0])
    max_v = max(arr[i][0], dp[i - 1][0][1])
    dp[i][0] = (min_v, max_v)

for i in range(1, n):
    min_v = min(arr[0][i], dp[0][i - 1][0])
    max_v = max(arr[0][i], dp[0][i - 1][1])
    dp[0][i] = (min_v, max_v)

for i in range(1,n):
    for j in range(1,n):
        min_v = max(min(arr[i][j], dp[i - 1][j][0]), min(arr[i][j], dp[i][j-1][0]))
        max_v = min(max(arr[i][j], dp[i - 1][j][1]), max(arr[i][j], dp[i][j-1][1]))

        dp[i][j] = (min_v, max_v)

print(dp[n-1][n-1][1] - dp[n-1][n-1][0])