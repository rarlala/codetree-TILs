n = int(input())
arr = list(map(int, input().split()))
result = 0

sum = 0
for i in range(n):
    if sum == 0:
        result = arr[i]    
    sum += arr[i]
    result = max(sum, result)
    
    if sum < 0:
        sum = 0
        continue

print(result)