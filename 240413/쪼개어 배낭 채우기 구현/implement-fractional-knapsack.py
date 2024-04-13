n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: -x[1] / x[0])
result = 0

for w, v in arr:
    if m >= w:
        m -= w
        result += v
    else:
        result += m / w * v
        break
    
print(f"{result:.3f}")