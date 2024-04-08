board = [list(map(int, input().split(" "))) for _ in range(19)]

win = 0
x, y = 0, 0
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            current = board[i][j]
            count = 1

            for k in range(1, 5):
                if win != 0:
                    break
                if i + k < 19 and board[i + k][j] == current:
                    count += 1
                else:
                    break
                if count == 3:
                    x, y = i + k + 1, j + 1
                if count == 5:
                    win = current
                    break
            
            count = 1
            for l in range(1, 5):
                if win != 0:
                    break
                if j + 1 < 19 and board[i][j + l] == current:
                    count += 1
                else:
                    break
                if count == 3:
                    x, y = i + 1, j + l + 1
                if count == 5:
                    win = current
                    break

            count = 1
            for m in range(1, 5):
                if win != 0:
                    break
                if i + m < 19 and j + m < 19 and board[i + m][j + m] == current:
                    count += 1
                else:
                    break
                if count == 3:
                    x, y = i + m + 1, j + m + 1
                if count == 5:
                    win = current
                    break

            count = 1
            for n in range(1, 5):
                if win != 0:
                    break
                if i - n < 19 and j - n < 19 and board[i - n][j + n] == current:
                    count += 1
                else:
                    break
                if count == 3:
                    x, y = i - n + 1, j + n + 1
                if count == 5:
                    win = current
                    break


if win != 0:
    print(win)
    print(x, y)
else:
    print(win)