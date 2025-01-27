import sys
read_line=sys.stdin.readline
arr=[]
for i in range(9):
    line= read_line().strip()
    arr.append(list(map(int, line.split())))

result=-1
x, y =0, 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > result:
            result = arr[i][j]
            x, y = i+1, j+1
print(result)
print(x, y)