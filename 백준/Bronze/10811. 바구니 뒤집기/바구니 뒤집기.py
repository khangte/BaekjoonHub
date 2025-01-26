n, m = map(int, input().split())
bucket = [i for i in range(n+1)]
for x in range(m):
    i, j = map(int, input().split())
    temp = bucket[i : j+1]
    temp.reverse()
    bucket[i: j+1] = temp

for z in range(1, n+1):
    print(bucket[z], end=' ')