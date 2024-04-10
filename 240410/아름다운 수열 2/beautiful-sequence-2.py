n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
for i in range(n):
    arr = set()
    for c in b:
        if c in a[i: i + m]:
            arr.add(a[i: i + m].index(c))
    if len(a[i: i + m]) == m and len(arr) == len(set(a[i: i + m])):
        count += 1

print(count)