c, n = map(int, input().split())
c_arr = [int(input()) for _ in range(c)]
n_arr = [tuple(map(int, input().split())) for _ in range(n)]
c_arr.sort(reverse = True)
n_arr.sort(key=lambda x: (-x[1], -x[0]))

c_idx = c - 1
n_idx = n - 1

result = 0
while 0 <= c_idx < c and 0 <= n_idx < n:
    a, b = n_arr[n_idx]
    t = c_arr[c_idx]

    if a <= t <= b:
        result += 1
        c_idx -= 1
        n_idx -= 1

    elif a > t:
        c_idx -= 1
    
    elif t > b:
        n_idx -= 1
    
print(result)