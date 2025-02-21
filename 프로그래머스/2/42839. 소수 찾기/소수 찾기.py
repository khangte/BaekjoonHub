import math
from itertools import permutations

def is_prime_number(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i==0:
            return False
    return True

def solution(numbers):
    number_list = list(numbers)
    permutation_set = set()
    
    for i in range(1, len(number_list)+1):
        for p in permutations(number_list, i):
            num = int(''.join(p))
            permutation_set.add(num)
            
    permutation_set.discard(0)
    permutation_set.discard(1)
    
    cnt = sum(1 for x in permutation_set if is_prime_number(x))
    return cnt