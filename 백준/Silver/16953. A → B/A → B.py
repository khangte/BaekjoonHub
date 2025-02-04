import sys
read_line = sys.stdin.readline

a, b = map(int, read_line().rstrip().split())
cnt = 1

while b != a:
    cnt += 1
    bb = b
    if (b%2) == 0:
        b = b//2
    elif (b%10) == 1:
        b = b//10
    if bb==b:
        print(-1)
        break
else: print(cnt)
