n=int(input())
array = list(map(int, input().split()))
v = int(input())
count =0
for k in array:
    if v==k:
        count+=1
print(count)
