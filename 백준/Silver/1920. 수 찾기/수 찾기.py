import sys
read_line = sys.stdin.readline

def binary_search(array, target):
    start, end = 0, len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return False

n = int(read_line().rstrip())
num_list1 = list(map(int, read_line().rstrip().split()))
m = int(read_line().rstrip())
num_list2 = list(map(int, read_line().rstrip().split()))

num_list1.sort()
for target in num_list2:
    if binary_search(num_list1, target):
        print(1)
    else:
        print(0)