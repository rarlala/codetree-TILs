n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(n):
    overlap = False

    for j in range(n):
        if i == j:
            continue

        if (arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]):
            overlap = True
            break
    if overlap == False:
        count += 1

print(count)