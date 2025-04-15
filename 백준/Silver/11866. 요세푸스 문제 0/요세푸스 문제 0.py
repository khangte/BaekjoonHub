n, k = map(int, input().split())

queue = [i for i in range(1, n+1)]
result = []
idx = 0
while queue:
    idx += k-1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(queue.pop(idx))

print("<%s>" %(', '.join(map(str, result))))
