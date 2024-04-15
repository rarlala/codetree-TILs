n = int(input())
b = {int(input()) for _ in range(n)}
a = [i for i in range(1, 2 * n + 1) if i not in b]

result = 0
a.sort()
b = sorted(b)

while a and b:
    if a[-1] > b[-1]:
        result +=1
        a.pop()
        b.pop()
    else:
        a.pop(0)
        b.pop()

print(result)