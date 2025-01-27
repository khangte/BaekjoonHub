import sys
from collections import deque

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    p = sys.stdin.readline().rstrip()  # 수행할 함수
    n = int(input())  # 배열에 들어 있는 수의 개수
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(',')) # []형식의 숫자 배열 입력

    reverse_flag = False

    if n == 0:
        arr=[]
    for x in p:
        if x == 'R':
            # arr.reverse() 매번 reverse()를 해주어야되기 때문에 시간초과 남
            reverse_flag = not reverse_flag
        elif x == 'D':
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if reverse_flag:
            arr.reverse()
        print("[" + ",".join(arr) + "]")