from itertools import permutations

n = int(input())

# 순열(itertools.permutations)을 사용하여 모든 경우의 수를 생성
baseballs = list(permutations([1,2,3,4,5,6,7,8,9], 3))

for _ in range(n):
    num, s_cnt, b_cnt = input().rstrip().split()
    s_cnt, b_cnt = int(s_cnt), int(b_cnt) # 스트라이크 수, 볼 수

    delete = [] # 조건에 맞지 않는 후보를 삭제할 목록
    for i in range(len(baseballs)):
        s, b = 0, 0 # 스트라이크와 볼 초기화
        for j in range(3): # num 각 자리에 대해 검사
            # 입력 숫자의 각 자리가 baseballs에 포함되어 있으면,
            if int(num[j]) in baseballs[i]: 
                if int(num[j]) == baseballs[i][j]: # 자릿수까지 같으면 스트라이크
                    s += 1
                else: # 숫자가 존재하지만 자릿수가 다르면 볼
                    b += 1
        
        # 입력된 스트라이크/볼 수와 다르면 제거 대상에 추가
        if s != s_cnt or b != b_cnt:
            delete.append(baseballs[i])
            
    # 조건에 맞지 않는 모든 후보 제거        
    for del_num in delete:
        baseballs.remove(del_num)

# 남은 후보의 개수를 출력
print(len(baseballs))
