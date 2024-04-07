r, c = map(int, input().split())
arr = [input().split() for _ in range(r)]
result = 0

for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[r - 1][c - 1]:
                    result += 1

print(result)