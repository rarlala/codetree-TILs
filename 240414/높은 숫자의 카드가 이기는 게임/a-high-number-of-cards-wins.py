n = int(input())
a = []
b = [int(input()) for _ in range(n)]
b.sort(reverse = True)

for i in range(2 * n, 1, -1):
    if i not in b:
        a.append(i)

result = 0
for j in range(n):
    if b[j] < a[0]:
        result = n - j + 1

print(result)