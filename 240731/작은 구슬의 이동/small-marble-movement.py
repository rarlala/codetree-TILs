n, t = list(map(int, input().split()))
r, c, d = input().split()

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

d_dic = {"U": 0, "D": 3, "R": 1, "L": 2}
dr = d_dic[d]

x, y = int(r), int(c)

for _ in range(t):
    nx, ny = x + dx[dr], y + dy[dr]

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny
    else:
        dr = 3 - dr

print(x, y)