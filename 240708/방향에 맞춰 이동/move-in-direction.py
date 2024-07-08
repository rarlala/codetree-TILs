dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

for i in range(int(input())):
    d, n = input().split(" ")

    if d == 'N':
        x = x + (dx[0] * int(n)) 
        y = y + (dy[0] * int(n))
    elif d == 'E':
        x = x + (dx[1] * int(n)) 
        y = y + (dy[1] * int(n))
    elif d == 'S':
        x = x + (dx[2] * int(n)) 
        y = y + (dy[2] * int(n))
    elif d == 'W':
        x = x + (dx[3] * int(n)) 
        y = y + (dy[3] * int(n))

print(x, y)