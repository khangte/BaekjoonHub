import sys
read_line = sys.stdin.readline

def dfs(graph, v, visited, cnt):
    visited[v] = True
    cnt.append(1)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, cnt)
    return cnt

n = int(read_line().rstrip())
m = int(read_line().rstrip())
computer = [[]for i in range(n+1)]
for i in range(m):
    a,b = map(int, read_line().rstrip().split())
    computer[a].append(b)
    computer[b].append(a)

visited=[False] * (n+1)
cnt = []
dfs(computer, 1, visited, cnt)
print(len(cnt)-1) # 1번 노드 제외
