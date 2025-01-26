# 테스트 케이스 개수가 정해지지 않았기 때문에
# try except를 사용한다

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        exit()