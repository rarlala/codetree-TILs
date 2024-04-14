n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            result = max(arr[j] - arr[i], result)

print(result)