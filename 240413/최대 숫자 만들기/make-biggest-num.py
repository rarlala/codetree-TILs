from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]
arr.sort(reverse = True)

def compare(x, y):
    if int(x + y) > int(y + x):
        return -1
    if int(x + y) < int(y + x):
        return 1
    return 0

arr.sort(key=cmp_to_key(compare))
print(("").join(arr))