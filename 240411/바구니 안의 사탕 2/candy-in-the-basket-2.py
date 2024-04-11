n, k = map(int, input().split())
arr = [0] * 101

for _ in range(n):
    candy, x = map(int, input().split())
    arr[x] += candy

result = 0
for c in range(100):
    if 0 <= c - k <= 100 and 0 <= c + k <= 100:
        result = max(result, sum(arr[c - k : c + k + 1]))
        
print(result)