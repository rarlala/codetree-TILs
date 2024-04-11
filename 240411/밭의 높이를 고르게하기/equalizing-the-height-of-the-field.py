n, h, t = map(int, input().split())
arr = list(map(int, input().split()))
result = 1e9

for i in range(n - t + 1):
    count = 0
    for j in arr[i : i + t]:
        if j == h:
            continue
        elif j > h:
            count += j - h
        elif j < h:
            count += h - j
    result = min(result, count)
print(result)