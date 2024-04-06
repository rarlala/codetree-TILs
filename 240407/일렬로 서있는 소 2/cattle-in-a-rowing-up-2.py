n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] <= arr[j] <= arr[k]:
                result += 1

print(result)