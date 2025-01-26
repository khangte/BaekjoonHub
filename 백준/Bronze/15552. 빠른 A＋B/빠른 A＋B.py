import sys

read_line=sys.stdin.readline
t=int(read_line().strip())

for i in range(t):
    a, b = map(int, read_line().split())
    print(a+b)