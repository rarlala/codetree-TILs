from functools import cmp_to_key

n = int(input())
brackets = []
score = 0

for _ in range(n):
    s = input()
    o_n, c_n = 0, 0

    for char in s:
        if char == "(":
            o_n += 1
        else:
            c_n += 1
            score += o_n

    brackets.append((o_n, c_n))

def compare(b1, b2):
    open1, closed1 = b1
    open2, closed2 = b2

    if open1 * closed2 > open2 * closed1:
        return -1
    if open1 * closed2 < open2 * closed1:
        return 1
    return 0

brackets.sort(key=cmp_to_key(compare))

open_sum = 0
for o_n, c_n in brackets:
    score += open_sum * c_n
    open_sum += o_n

print(score)