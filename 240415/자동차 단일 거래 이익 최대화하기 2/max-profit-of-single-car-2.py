n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        result = max(result, arr[j] - arr[i])

print(result)