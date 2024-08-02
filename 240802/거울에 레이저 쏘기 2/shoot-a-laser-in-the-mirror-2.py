n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

x, y = 0, 0

# k -> k // n
# 북 동 남 서
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

#    1  2  3
# 12 00 01 02 4
# 11 10 11 12 5
# 10 20 21 22 6
#     9  8  7

dir_num = (k - 1) // n
# 북 -> x = 0, y = k - 1
# 동 -> x = (n * 2) - (n + 1), y = n - 1
# 남 -> x = n - 1, y = (n * 3) - k
# 서 -> x = (n * 4) - 1 , y = 0
if dir_num == 0:
    x, y = 0, k - 1
elif dir_num == 1:
    x, y = (n * 2) - (n + 1), n - 1
elif dir_num == 2:
    x, y = n - 1,(n * 3) - k
else:
    x, y = (n * 4) - 1, 0

count = 0
check = True

while check:
    count += 1
    # /
    # 북쪽 -> 서쪽
    # 서쪽 -> 북쪽
    # 동쪽 -> 남쪽
    # 남쪽 -> 동쪽
    if arr[x][y] == '/':
        if dir_num == 0: # 북
            x, y = x + dx[3], y + dy[3]
            dir_num = 3
        elif dir_num == 1: # 동
            x, y = x + dx[2], y + dy[2]
            dir_num = 2
        elif dir_num == 2: # 남
            x, y = x + dx[1], y + dy[1]
            dir_num = 1
        else: # 서
            x, y = x + dx[0], y + dy[0]
            dir_num = 0
    # \
    # 북쪽 -> 서쪽
    # 동쪽 -> 남쪽
    # 서쪽 -> 북쪽
    # 남쪽 -> 동쪽
    elif arr[x][y] == '\\':
        if dir_num == 0: # 북
            x, y = x + dx[3], y + dy[3]
            dir_num = 3
        elif dir_num == 1: # 동
            x, y = x + dx[2], y + dy[2]
            dir_num = 2
        elif dir_num == 2: # 남
            x, y = x + dx[1], y + dy[1]
            dir_num = 1
        else: # 서
            x, y = x + dx[0], y + dy[0]
            dir_num = 0

    if not 0 <= x < n and 0 <= y < n:
        check = False

print(count)