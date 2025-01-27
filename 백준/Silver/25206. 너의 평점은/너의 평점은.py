import sys
read_line = sys.stdin.readline
arr=[list(read_line().strip().split()) for i in range(20)]

sum_sub=0
multi_credit_grade=0
for i in range(20):
    grade = arr[i][2] # 성적
    if grade == 'A+': arr[i][2] = float(4.5)
    elif grade == 'A0': arr[i][2] = float(4.0)
    elif grade == 'B+': arr[i][2] = float(3.5)
    elif grade == 'B0': arr[i][2] = float(3.0)
    elif grade == 'C+': arr[i][2] = float(2.5)
    elif grade == 'C0': arr[i][2] = float(2.0)
    elif grade == 'D+': arr[i][2] = float(1.5)
    elif grade == 'D0': arr[i][2] = float(1.0)
    elif grade == 'F' : arr[i][2] = float(0.0)

    if grade != 'P':
        sum_sub += float(arr[i][1])  # 학점 총합
        multi_credit_grade += float(arr[i][1]) * arr[i][2] # 학점*과목 평점의 총합
        
print(multi_credit_grade/sum_sub)