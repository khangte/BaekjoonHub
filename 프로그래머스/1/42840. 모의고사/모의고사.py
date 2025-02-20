def solution(answers):
    h1 = [1, 2, 3, 4, 5]
    h2 = [2, 1, 2, 3, 2, 4, 2, 5]
    h3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0 for _ in range(4)]
    for i in range(len(answers)):
        if answers[i] == h1[i%5]:
            score[1] += 1
        if answers[i] == h2[i%8]:
            score[2] += 1
        if answers[i] == h3[i%10]:
            score[3] +=1
    max_score = max(score)
    answer = [i for i in range(1, len(score)) if max_score == score[i]]
    return answer