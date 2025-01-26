n, k = input().split()
n = int(n)
count=0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if k in f"{h:02}{m:02}{s:02}":
                count+=1
print(count)