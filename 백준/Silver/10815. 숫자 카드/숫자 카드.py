import sys
input = sys.stdin.readline

def binary_search(array, target, start: int, end: int):
    if start > end:
        return None
    mid = (start + end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 상근이가 갖고있는 숫자카드 개수
n = int(input())
# 상근이가 갖고있는 숫자카드 정수
n_list = list(map(int, input().split()))
n_list_array = sorted(n_list)

# 맞출 숫자 개수
m = int(input())
# 맞출 정수
m_list = list(map(int, input().split()))

for i in m_list:
    result = binary_search(n_list_array, i, 0, n-1)
    if result is None:
        print("0")
    else: 
        print("1")
