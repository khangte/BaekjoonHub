import sys
read_line = sys.stdin.readline

n, m = map(int,read_line().rstrip().split())

arr = []

def backtracking():
    if len(arr) == m:
        print(' '.join(map(str, arr)))

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()