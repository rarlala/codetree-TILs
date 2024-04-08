n = int(input())
arr = [int(input()) for i in range(n)]
data = [0] * n

result = 1e9

for i in range(n):
    sum = 0
    num = 0
    for j in range(n):
        num = (n - (i - j)) % n
        sum += arr[j] * num
    result = min(sum, result)
    
print(result)