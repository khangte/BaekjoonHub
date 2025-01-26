a=[]
for i in range(9):
    n=int(input())
    a.append(n)
print(max(a))
for i in range(9):
    if max(a)==a[i]:
        print(i+1)
