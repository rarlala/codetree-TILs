move = list(input())

x, y = 0, 0
direction = "N"
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# NESW
for a in move:
    if a == "L":
        if direction == "N":
            direction = "W"
        elif direction == "E":
            direction = "N"
        elif direction == "W":
            direction = "S"
        else:
            direction = "E"
    elif a == "R":
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "W":
            direction = "N"
        else:
            direction = "W"
    else:
        if direction == "E":
            move_dir = 0
        elif direction == "W":
            move_dir = 1
        elif direction == "S":
            move_dir = 2
        else:
            move_dir = 3

        x += dx[move_dir]
        y += dy[move_dir]

print(x, y)