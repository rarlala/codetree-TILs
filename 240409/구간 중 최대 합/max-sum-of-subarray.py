n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(n - 2):
    result = max(result, arr[i] + arr[i+1] + arr[i+2])

print(result)