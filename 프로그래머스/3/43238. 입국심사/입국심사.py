def solution(n, times):
    left, right = min(times), max(times) * n # 가능한 최소, 최대 시간
    
    while left <= right:
        mid = (left + right) // 2 # 중간값 (심사에 걸리는 시간)
        total = sum(mid//time for time in times) # 해당 시간 내에 심사 가능한 인원 수 계산
        
        if total >= n: # n명을 모두 처리할 수 있다면 시간을 줄여본다.
            answer = mid
            right = mid - 1
        else: # 처리할 수 없다면 시간을 늘려야 한다.
            left = mid + 1
    return answer