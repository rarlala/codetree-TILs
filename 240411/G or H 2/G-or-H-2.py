n = int(input())
arr = [0] * 101
max_idx = 0
for _ in range(n):
    x, a = input().split()
    arr[int(x)] = a
    max_idx = max(max_idx, int(x))

result = 0
for i in range(max_idx + 1):
    if arr[i] == 0:
        continue
    for j in range(max_idx + 1):
        if arr[j] == 0:
            continue
        
        g_c = arr[i:j + 1].count("G")
        h_c = arr[i:j + 1].count("H")

        if g_c != 0 and g_c == h_c:
            result = max(result, j - i)
        elif (g_c > 0 and h_c == 0) or (g_c == 0 and h_c > 0):
            result = max(result, j - i)

print(result)