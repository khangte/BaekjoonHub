import sys
sys.setrecursionlimit(10000)

def dfs(computers, v, visited, n):
    visited[v] = True
    for i in range(n):
        if computers[v][i] == 1 and not visited[i]:
            dfs(computers, i, visited, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited, n)
            answer += 1
    return answer