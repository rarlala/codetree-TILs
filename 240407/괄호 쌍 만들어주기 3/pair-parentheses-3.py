arr = input()
result = 0

for i in range(len(arr)):
    if arr[i] == "(":
        for j in range(i + 1, len(arr)):
            if arr[j] == ")":
                result += 1

print(result)