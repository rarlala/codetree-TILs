n, m = list(map(int, input().split()))
arr = [[0] * m for _ in range(n)]

num = 1
dr = 0
x, y = 0, 0

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(n * m):
    arr[x][y] = num
    num += 1
    
    nx, ny = x + dx[dr], y + dy[dr]

    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dr = (dr + 1) % 4
        nx, ny = x + dx[dr], y + dy[dr]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            x, y = nx, ny
        
for i in arr:
    print(*i)