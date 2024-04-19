import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

min_result = sys.maxsize

for i in range(n):
    result = sys.maxsize
    for j in range(n):
        if i == j:
            continue

        x1, y1 = arr[i]
        x2, y2 = arr[j]

        result = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        min_result = min(result, min_result)

print(min_result)