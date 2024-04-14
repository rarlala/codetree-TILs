n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(n - 1):
    if max(arr[i+1:n]) > arr[i]:
        result = max(result, max(arr[i+1:n]) - arr[i])
    
print(result)