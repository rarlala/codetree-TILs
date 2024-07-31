arr = [list(map(int, input().split())) for _ in range(int(input()))]

dxs = [0, 0, 1, -1]
dys = [-1, 1, 0, 0]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        check = 0

        for dx, dy in zip(dxs, dys):
            if 0 <= i + dx < len(arr) and 0 <= j + dy < len(arr):
                if arr[i + dx][j + dy] == 1:
                    check += 1
        
        if check >= 3:
            count += 1

print(count)