n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [0, -1, 0, 1, -1, -1, 1, 1]
dy = [-1, 0, 1, 0, -1, 1, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        for x, y in zip(dx, dy):
            cnt = 0
            for k in range(3):
                nx = i + (x * k)
                ny = j + (y * k)

                if 0 <= nx < n and 0 <= ny < m:
                    if k == 0 and arr[nx][ny] == "L":
                        cnt += 1
                    elif (k == 1 or k == 2) and arr[nx][ny] == "E":
                        cnt += 1
                    else:
                        break
            if cnt == 3:
                result += 1

print(result)