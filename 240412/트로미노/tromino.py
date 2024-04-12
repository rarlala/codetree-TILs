n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if 0 <= i + 1 < n and 0 <= j + 1 < m:
            a = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1]
            b = arr[i][j] + arr[i][j + 1] + arr[i + 1][j]
            c = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            result = max(a, b, c, result)
        if 0 <= i + 1 < n and 0 <= j - 1 < m:
            d = arr[i][j] + arr[i + 1][j] + arr[i + 1][j - 1]
            result = max(d, result)
        if 0 <= j + 2 < m:
            e = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            result = max(e, result)
        if 0 <= i + 2 < n:
            f = arr[i][j] + arr[i + 1][j] + arr[i + 2][j]
            result = max(f, result)

print(result)