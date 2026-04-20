def solution(numbers):
    total_len = 45
    answer = 0
    for i in numbers:
        answer += i
    answer = total_len - answer
    return answer