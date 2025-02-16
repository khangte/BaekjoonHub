import sys

num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()

for i in num:
    print(i, end=' ')