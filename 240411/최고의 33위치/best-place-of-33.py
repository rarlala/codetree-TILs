n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
if n == 3:
    for i in arr:
        result += sum(i)
else:
    for i in range(n - 3):
        for j in range(n - 3):
            sum = 0
            
            for k in range(3):
                for l in range(3):
                    sum += arr[i+k][j+l]
        
    result = max(result, sum)

print(result)