n = int(input())
ans = 0

nums = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    nums.append((y, x))

nums.sort()

li, ri = 0, n - 1
while li <= ri:
    ly, lx = nums[li]
    ry, rx = nums[ri]

    ans = max(ans, ly + ry)

    if lx < rx:
        nums[ri] = (ry, rx - lx)
        li += 1
    elif lx > rx:
        nums[li] = (ly, lx - rx)
        ri -= 1
    else:
        li += 1
        ri -= 1
    
print(ans)