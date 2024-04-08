n = int(input())
arr = list(input())

count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] == "C" and arr[j] == "O" and arr[k] == "W":
                count += 1

print(count)