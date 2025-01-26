n=int(input())
result=0
for i in range(n+1):
    nums = list(map(int, str(i))) # 각 자리수를 구함
    result = sum(nums) + i # 분해자 = 각 자리수의 총합 + 생성자
    if result == n:
        print(i)
        break
    if i==n: print(0)