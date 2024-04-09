n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n - 2):
        one = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

        for k in range(i, n):
            if k == i:
                if n >= 6:
                    for l in range(j + 3, n - 2):
                        two = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                        result = max(result, one + two)
            else:
                for l in range(j, n - 2):
                    two = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                    result = max(result, one + two)

print(result)