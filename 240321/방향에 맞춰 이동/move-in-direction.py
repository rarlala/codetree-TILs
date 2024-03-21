x, y = 0, 0
for _ in range(int(input())):
    d, n = input().split()
    if d == "E":
        x = x + int(n)
    elif d == "W":
        x = x - int(n)
    elif d == "S":
        y = y - int(n)
    elif d == "N":
        y = y + int(n)

print(x, y)