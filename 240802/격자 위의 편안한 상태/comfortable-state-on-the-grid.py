n, m = list(map(int, input().split()))
arr = [[0] * n for i in range(n)]

dxs, dys = [0,0,1,-1], [1,-1,0,0]

for _ in range(m):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    arr[x][y] = 1

    count = 0
    for (dx, dy) in zip(dxs, dys):
        if 0 <= x + dx < n and 0 <= y + dy < n and arr[x + dx][y + dy] == 1:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)