n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i + 2, n):
        result = max(result, arr[i] + arr[j])

print(result)