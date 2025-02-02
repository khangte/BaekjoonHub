from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 여기선 x가 상/하, y가 좌/우
#               상      하      좌      우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if graph[nx][ny]==1:
                graph[nx][ny]=-1
                dfs(nx, ny)

t = int(input().rstrip())

for _ in range(t):
    m, n, k = map(int, input().rstrip().split()) # 가로, 세로, 배추 개수
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1 # 배추가 심어진 곳

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
