r, c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]
result = 0

stack = [[0, 0, 0]]
while stack:
    x, y, check = stack.pop()
    for i in range(x + 1, r):
        for j in range(y + 1, c):
            if i == r - 1 and j == c - 1:
                result += 1
            if arr[i][j] != arr[x][y] and check < 2:
                stack.append([i, j, check + 1])
                break
            
print(result)