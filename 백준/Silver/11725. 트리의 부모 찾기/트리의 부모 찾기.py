from collections import deque
import sys
read_line = sys.stdin.readline

n = int(read_line().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, read_line().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
parent_node = [0] * (n+1)
visited = [False] * (n+1)
while queue:
    a = queue.popleft()
    visited[a] = True
    for node in graph[a]:
        if not visited[node]:
            if node is not None:
                parent_node[node] = a
                queue.append(node)

for i in range(2, n+1):
    print(parent_node[i])
