n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = sum(arr)
result = 10001

for i in range(n):
    for j in range(i + 1, n):
        result = min(result, abs(s - (arr_sum - arr[i] - arr[j])))

print(result)