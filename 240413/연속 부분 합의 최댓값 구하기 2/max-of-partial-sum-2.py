n = int(input())
arr = list(map(int, input().split()))
result = max(arr)

for i in range(n):
    sum = arr[i]
    
    for j in range(i + 1, n):
        sum += arr[j]    
        if sum >= result:
            result = sum
        else:
            break

print(result)