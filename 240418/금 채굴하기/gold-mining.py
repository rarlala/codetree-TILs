n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def get_area(k):
    return k * k + (k + 1) * (k + 1) 

def get_num_of_gold(row, col, k):
    return sum([
        arr[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row - i) + abs(col - j) <= k
    ])

max_gold = 0

for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)

            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)