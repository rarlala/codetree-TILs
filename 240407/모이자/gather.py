n = int(input())
arr = list(map(int, input().split()))
min_sum = 1e9

for i in range(n):
    sum = 0
    for j in range(n):
        if i != j:
           sum += arr[j] * abs(j - i)
    min_sum = min(min_sum, sum)

print(min_sum)