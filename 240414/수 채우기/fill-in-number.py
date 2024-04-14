n = int(input())
arr = [1e9] * (n + 1)
arr[2] = 1
arr[5] = 1

for i in range(1, n + 1):
    arr[i] = min(arr[i - 2] + 1, arr[i])
    arr[i] = min(arr[i - 5] + 1, arr[i])

print(arr[n])