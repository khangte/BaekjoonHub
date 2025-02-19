from collections import Counter

def solution(participant, completion):
    counts = Counter(participant)
    for c in completion:
        counts[c] -= 1
    for p in counts:
        if counts[p] > 0:
            return p