n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)

count = 0
for i in range(n):
    if arr[i] <= k:
        num = k // arr[i]
        k -= arr[i] * num
        count += num

print(count)