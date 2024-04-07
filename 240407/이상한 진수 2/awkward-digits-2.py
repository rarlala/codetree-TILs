n = list(input())
check = False

for i in range(len(n)):
    if n[i] == "0" and check == False:
        n[i] = "1"
        check = True
        break

if not check:
    n[len(n) - 1] = 0

result = 0
idx = len(n) - 1
for i in range(len(n)):
    result += int(n[i]) * (2 ** idx)
    idx -= 1

print(result)