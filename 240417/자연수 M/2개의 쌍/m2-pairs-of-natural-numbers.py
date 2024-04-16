n = int(input())
arr = []

for _ in range(n):
    x, y = tuple(map(int, input().split()))

    for _ in range(x):
        arr.append(y)

arr.sort()
ans = 1e9

f_idx = 0
e_idx = n

for i in range(n // 2):
    f_idx += 1
    e_idx -= 1

    if f_idx != e_idx and ans > arr[f_idx] + arr[e_idx]:
        ans = arr[f_idx] + arr[e_idx]
        
print(ans)