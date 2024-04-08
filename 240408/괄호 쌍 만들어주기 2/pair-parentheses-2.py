arr = list(input())

count = 0
for i in range(len(arr)):
    for j in range(i + 2, len(arr) - 1):
        if arr[i] == "(" and arr[i + 1] == "(" and arr[j] == ")" and arr[j + 1] == ")":
            count += 1

print(count)