# 7568번

n = int(input())

data = []
ans = []

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    rank = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank += 1
    ans.append(rank + 1)

for d in ans:
    print(d, end=' ')
