n = int(input())
arr = list(map(int, input().split()))
result = 0

min_v = 100000
for i in range(n):
    min_v = min(min_v, arr[i])
    result = max(result, arr[i] - min_v)

print(result)