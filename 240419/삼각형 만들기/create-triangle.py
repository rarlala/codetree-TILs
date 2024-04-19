n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_result = 0
for i in range(n):
    result = 0
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            x3, y3 = arr[k]

            if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
                result = abs(((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x2 * y1) + (x3 * y2) + (x1 * y3)))

            max_result = max(max_result, result)

print(max_result)