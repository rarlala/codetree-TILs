x, y = 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(int(input())):
    d, n = input().split()
    n = int(n)

    if d == "E":
        dir = 0
    elif d == "W":
        dir = 1
    elif d == "N":
        dir = 2
    else:
        dir = 3

    x += dx[dir] * n
    y += dy[dir] * n

print(x, y)