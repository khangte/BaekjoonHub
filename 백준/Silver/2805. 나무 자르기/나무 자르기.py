import sys
read_line = sys.stdin.readline

n,m = map(int, read_line().rstrip().split())
trees = list(map(int, read_line().rstrip().split()))

start, end = 0, max(trees)
result=0
while start <= end:
    mid = (start + end)//2
    tree_len = sum(tree-mid for tree in trees if tree>mid)

    if tree_len < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)