n,m=map(int, input().split())
bucket = [0] * (n+1)
for x in range(1, n+1):
    bucket[x] = x

for y in range(m):
    i, j = map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]

for z in range(1, n+1):
    print(bucket[z], end=' ')