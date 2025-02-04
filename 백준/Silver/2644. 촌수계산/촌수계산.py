from collections import deque
import sys
read_line = sys.stdin.readline

n = int(read_line().rstrip())
x, y = map(int, read_line().rstrip().split())
m = int(read_line().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, read_line().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([x])
cnt = [0] * (n+1)
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if cnt[next_node] == 0:
            cnt[next_node] = cnt[now] + 1
            queue.append(next_node)

if cnt[y] == 0: print(-1)
else: print(cnt[y])