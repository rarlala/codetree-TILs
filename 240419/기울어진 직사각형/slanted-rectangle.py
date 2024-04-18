n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

max_result = 0

for i in range(n - 1, 0, -1):
    for j in range(1, n - 1):
        cur_sum = arr[i][j]

        x, y = i, j
        idx = 0
        cnt = 0

        while idx < 4:
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx == i and ny == j:
                break
            elif 0 <= nx < n and 0 <= ny < n:
                cur_sum += arr[nx][ny]
                x, y = nx, ny
                cnt += 1
            else:
                idx += 1
                if cnt == 0:
                    cur_sum = 0
                    break
                cnt = 0
            
        max_result = max(max_result, cur_sum)

print(max_result)