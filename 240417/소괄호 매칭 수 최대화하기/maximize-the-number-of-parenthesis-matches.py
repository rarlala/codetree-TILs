n = int(input())
arr = []

for _ in range(n):
    data = list(input())
    l = data.count("(")
    r = data.count(")")
    arr.append((l, r, data))

arr.sort(key=lambda x: (-x[0], x[1]))

str_arr = []
for data in arr:
    for j in data[2]:
        str_arr.append(j)

score = 0
for i in range(len(str_arr)):
    for j in range(i + 1, len(str_arr)):
        if str_arr[i] == "(" and str_arr[j] == ")":
            score += 1

print(score)