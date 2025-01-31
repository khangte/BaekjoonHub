from collections import deque
import sys
read_line = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print (v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, read_line().rstrip().split())
# n 정점의 개수, m 간선의 개수, v 탐색을 시작할 정점의 번호
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, read_line().rstrip().split())
    graph[a].append(b)
    graph[b].append(a) # 방향이 없는 간선이므로 추가

for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)