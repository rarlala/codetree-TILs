n = int(input())
a = []
b = [int(input()) for _ in range(n)]
b.sort(reverse = True)

for i in range(2 * n, 1, -1):
    if i not in b:
        a.append(i)

result = 0
for j in range(n):
    for k in range(len(a)):
        if b[j] < a[k]:
            result += 1
            a.pop(k)
            break

print(result)