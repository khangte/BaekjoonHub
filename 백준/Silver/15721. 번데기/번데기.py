a = int(input()) # 인원 수
t = int(input()) # T번 째
x = int(input()) # 뻔 0 데기 1

turn=0
cnt=0
arr_len=0
while True:
    for i in range(4):
        arr_len+=1
        if x == (i % 2):
            cnt+=1
        if cnt==t:
            print((arr_len-1)%a)
            exit()

    turn += 1
    for i in range(turn+1):
        arr_len+=1
        if x==0:
            cnt+=1
        if cnt==t:
            print((arr_len-1)%a)
            exit()
    for i in range(turn+1):
        arr_len+=1
        if x==1:
            cnt+=1
        if cnt==t:
            print((arr_len-1)%a)
            exit()
