import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            graph[nx][ny]=-1
            dfs(nx, ny)

while True:
    w, h = map(int, input().rstrip().split()) # w 지도의 너비, h 지도의 높이
    if w==0 and h==0: break
    
    graph = [list(map(int, input().rstrip().split())) for _ in range(h)]
    cnt=0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt+=1
    print(cnt)
