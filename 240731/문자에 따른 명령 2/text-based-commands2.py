# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

text = input()
dr = 0

for i in range(len(text)):
    if text[i] == 'L':
        dr = (dr + 3) % 4
    elif text[i] == 'R':
        dr = (dr + 1) % 4
    else:
        x, y = x + dx[dr], y + dy[dr]

print(x, y)