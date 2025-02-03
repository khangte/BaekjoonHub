import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip()) # 층수
    n = int(input().rstrip()) # 호수

    d = [[0] * (n+1) for _ in range(k+1)] # DP 테이블
    for i in range(1, n+1):
        d[0][i] = i

    for x in range(1, k+1): # 1층부터 k층까지
        for y in range(1, n+1): #1호부터 n호까지
            d[x][y] = d[x-1][y] + d[x][y-1]
    print(d[k][n])