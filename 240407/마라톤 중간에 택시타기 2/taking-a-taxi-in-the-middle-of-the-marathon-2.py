n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 1e9

for i in range(1, n - 1):
    sum = 0
    prev = 0
    for j in range(n):
        if i == j:
            continue
        sum += (abs(arr[prev][0] - arr[j][0]) +  abs(arr[prev][1] - arr[j][1]))
        prev = j
    
    result = min(sum, result)

print(result)