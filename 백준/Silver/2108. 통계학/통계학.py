from collections import Counter
import sys

read_line = sys.stdin.readline
n=int(read_line())

if n%2==0: exit()

nums = [int(read_line().rstrip()) for i in range(n)]
print(round(sum(nums)/n))

nums.sort()
print(nums[(n//2)])

counter = Counter(nums)
max_freq = max(counter.values())
modes = [key for key, value in counter.items() if value==max_freq]
modes.sort()
print(modes[1] if len(modes)>1 else modes[0])

print(max(nums)-min(nums))