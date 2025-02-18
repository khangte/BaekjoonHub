import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, v):
    q = deque()
    q.append((v, 0))
    visited = [False] * (len(graph))
    visited[v] = True
    cnt = 0

    while q:
        x, depth = q.popleft()

        if depth >= 2: continue

        for i in graph[x]:
            if not visited[i]:
                q.append((i, depth+1))
                visited[i] = True
                cnt += 1
    return cnt

n = int(input().rstrip())
m = int(input().rstrip())

friendship = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    friendship[a].append(b)
    friendship[b].append(a)

print(bfs(friendship, 1))