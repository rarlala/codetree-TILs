n, k = map(int, input().split())
arr = [0] * 101

for _ in range(n):
    candy, x = map(int, input().split())
    arr[x] += candy

result = 0
for c in range(100):
    sum_all = 0
    for j in range(i - k, i + k + 1):
        if j >= 0 and j <= 100:
            sum_all += arr[i]
    result = max(result, sum_all)
        
print(result)