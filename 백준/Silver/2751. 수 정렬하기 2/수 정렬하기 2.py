import sys
input = sys.stdin.readline
n = int(input())
arr= [int(input()) for i in range(n)]
arr.sort()
for x in arr:
    print(x)