n = int(input())
arr = []
num_arr = []

for _ in range(n):
    data = list(input())
    l = data.count("(")
    r = data.count(")")
    arr.append((l, r, data))
arr.sort(key=lambda x: (-x[0], x[1]))

num = 0
for i in arr:
    for j in i[2]:
        if j == "(":
            num_arr.append(1)
        else:
            num_arr.append(0)

score = 0
for i in range(len(num_arr) - 1):
    if num_arr[i] == 1:
        score += num_arr[i+1:len(num_arr)].count(0)

print(score)