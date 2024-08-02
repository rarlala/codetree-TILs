time = 0
x, y = 0, 0
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
result = -1

for i in range(1, int(input()) + 1):
    dir, num = input().split()
    dir_num = 0

    if dir == 'N':
        dir_num = 0
    elif dir == 'S':
        dir_num = 1
    elif dir == 'E':
        dir_num = 2
    else:
        dir_num = 3
        
    for _ in range(int(num)):
        x, y = x + dx[dir_num], y + dy[dir_num]
        time += 1

        if x == 0 and y == 0:
            result = time
            break
        
        if result != -1:
            break
        

print(result)