n = int(input())
arr = [1e9] * (n + 1)
if n >= 2:
    arr[2] = 1
if n >= 5:
    arr[5] = 1

for i in range(1, n + 1):
    if n >= 2:
        arr[i] = min(arr[i - 2] + 1, arr[i])
    if n >= 5:
         arr[i] = min(arr[i - 5] + 1, arr[i])

print(-1 if arr[n] == 1e9 else arr[n])