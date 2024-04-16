n = int(input())
arr = []

for _ in range(n):
    x, y = tuple(map(int, input().split()))

    for _ in range(x):
        arr.append(y)

arr.sort()
ans = 1e9

for i in range(n // 2):
    a = arr.pop()
    b = arr.pop(0)

    ans = min(ans, a + b)

print(ans)