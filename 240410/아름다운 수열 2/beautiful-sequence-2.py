n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
count = 0
for i in range(n):
    temp_a = a[i: i + m]
    temp_a.sort()
    
    check = 0
    for j in range(m):
        if len(temp_a) == m and b[j] == temp_a[j]:
            check += 1
    if check == m:
        count += 1

print(count)