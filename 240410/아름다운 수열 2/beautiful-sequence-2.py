n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    check = True
    for c in b:
        if c not in a[i: i + m]:
            check = False
    if len(a[i: i + m]) == m and check:
        count += 1

print(count)