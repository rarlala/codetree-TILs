x, y = map(int, input().split())
answer = 0

for i in range(x, y + 1):
    sum = 0
    for j in str(i):
        sum += int(j)
        answer = max(sum, answer)

print(answer)