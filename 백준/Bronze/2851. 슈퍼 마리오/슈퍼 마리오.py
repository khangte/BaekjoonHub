result = 0
score_arr = [[0], [0]]

score_list = [int(input().rstrip()) for _ in range(10)]

for score in score_list:
    score_arr[0] = result
    result += score
    score_arr[1] = result
    if result >= 100:
        break

if abs(score_arr[0] - 100) >= abs(score_arr[1] - 100):
    print(score_arr[1])
else:
    print(score_arr[0])
