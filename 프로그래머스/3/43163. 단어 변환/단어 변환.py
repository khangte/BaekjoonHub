from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    visited = set()
    
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
    
        for word in words:
            if word not in visited and is_one_letter_diff(current, word):
                visited.add(word)
                queue.append((word, steps + 1))
        
def is_one_letter_diff(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1
        
def solution(begin, target, words):
    if target not in words: 
        return 0
    else:
        return bfs(begin, target, words)