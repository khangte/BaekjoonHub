from collections import Counter
import sys
read_line = sys.stdin.readline

def binary_search(arr, target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n = int(read_line().rstrip())
card_list = list(map(int, read_line().rstrip().split()))
m=int(read_line().rstrip())
cards = list(map(int, read_line().rstrip().split()))

counter = Counter(card_list)
card_list = list(set(card_list))
card_list.sort()
for target in cards:
    if binary_search(card_list, target):
        print(counter[target], end=' ')
    else:
        print(0, end=' ')