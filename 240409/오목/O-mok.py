import sys
arr = [list(map(int, input().split())) for _ in range(19)]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

dxs = [1, 1, 1, -1, -1, -1, 0, 0]
dys = [-1, 0, 1, -1, 0, 1, -1, 1]

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue

        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j

            while True:
                nx = curx + dx
                ny = cury + dy
                if in_range(nx, ny) == False:
                    break
                if arr[nx][ny] != arr[i][j]:
                    break
                curt += 1
                curx, cury = nx, ny

            if curt == 5:
                print(arr[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)