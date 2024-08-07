n, m = list(map(int, input().split()))
arr = [[0] * m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir = 0

for i in range(1, n * m + 1):
    arr[x][y] = i

    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
        x, y = nx, ny

for d in arr:
    print(*d)