n, m = map(int, input().split())
arrayA, arrayB = [], []
for i in range(n):
    data = list(map(int, input().split()))
    arrayA.append(data)
for i in range(n):
    data = list(map(int, input().split()))
    arrayB.append(data)
for i in range(n):
    for j in range(m):
        result = arrayA[i][j]+arrayB[i][j]
        print(result, end=' ')
    print('')