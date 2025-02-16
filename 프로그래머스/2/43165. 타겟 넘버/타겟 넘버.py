def dfs(numbers, target, idx, values):
    global cnt
	
    if idx == len(numbers):
        if values == target : 
            cnt += 1
        return
    
    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])
    
def solution(numbers, target) : 
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    return cnt