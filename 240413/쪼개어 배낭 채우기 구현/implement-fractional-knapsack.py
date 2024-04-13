n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = []

for w, v in arr:
    new_arr.append([v / w, w, v])
new_arr.sort(reverse = True)

result = 0
bag_m = 0
for a, v, w in new_arr:
    max_v, max_w = 0, 0

    for i in range(1, v + 1):
        if bag_m + i <= m:
            max_v = max(max_v, a * i)
            max_w = max(max_w, i)

    result += max_v
    bag_m += max_w
    
print(f"{result:.3f}")