n = int(input())
a = []
b = [int(input()) for _ in range(n)]
b.sort()

for i in range(1, 2 * n + 1):
    if i not in b:
        a.append(i)

result = 0

for i in range(len(b)):
    if len(a) == 0:
        break
    if max(a) > b[-1]:
        result += 1
        a.pop()
        b.pop()
    else:
        a.pop(0)
        b.pop()

print(result)