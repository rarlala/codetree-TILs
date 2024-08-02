dir_str = input()

x, y = 0, 0
dx, dy = [0,1,0,-1], [-1,0,1,0]
result = -1
dir_num = 0
time = 0

for str in dir_str:
    time += 1

    if str == 'L':
        dir_num = (dir_num + 3) % 4
    elif str == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]
        if x == 0 and y == 0 and result == -1:
            result = time

print(result)