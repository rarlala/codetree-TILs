n, k = map(int, input().split())
arr = []

max_num = 0
for _ in range(n):
    n, a = input().split()
    n = int(n)
    arr.append((n, a))
    max_num = max(max_num, n)

num_arr = [0] * max_num
for data in arr:
    idx, alpha = data
    num_arr[idx - 1] = 1 if alpha == "G" else 2

result = 0
for i in range(max_num - k):
    sum_k = sum(num_arr[i:i+k+1])
    result = max(result, sum_k)

print(result)