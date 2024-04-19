n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_result = 1e9
for i in range(n):
    result = 0
    xs = []
    ys = []
    for j in range(n):
        if i == j:
            continue
        
        x, y = arr[j]
        xs.append(x)
        ys.append(y)

    x1, x2, y1, y2 = min(xs), max(xs), min(ys), max(ys)
    result = (x2 - x1) * (y2 - y1)
    min_result = min(result, min_result)

print(min_result)