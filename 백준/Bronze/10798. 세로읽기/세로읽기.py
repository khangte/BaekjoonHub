import sys
read_line=sys.stdin.readline
arr=[read_line().strip() for i in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')