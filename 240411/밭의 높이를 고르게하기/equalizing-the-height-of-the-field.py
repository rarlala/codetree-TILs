n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

result = 1e9
for i in range(n - t - 1):
    count = 0
    for j in arr[i: i + t]:
        if arr[j] == h:
            continue
        elif arr[j] > h:
            count += arr[j] - h
        elif arr[j] < h:
            count += h - arr[j]
    result = min(result, count)
print(result)