n, k = map(int, input().split())
arr = [0] * 200
max_idx = 0
for _ in range(n):
    a, b = map(int, input().split())
    arr[b] += a
    max_idx = max(max_idx, a)

result = 0
for i in range(max_idx):
    if 0 <= i - k < max_idx and 0 <= i + k < max_idx:
        result = max(result, sum(arr[i - k : i + k + 1]))

print(result)