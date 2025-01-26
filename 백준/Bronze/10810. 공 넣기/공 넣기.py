n, m = map(int, input().split())
bucket = [0] * (n+1)
for x in range(m):
    i, j, k = map(int, input().split())
    for y in range(i, j+1):
        bucket[y] = k
for z in range(1, n+1):
    print(bucket[z], end=' ')