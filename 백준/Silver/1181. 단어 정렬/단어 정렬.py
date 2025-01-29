import sys
read_line = sys.stdin.readline

n = int(read_line())
word = [read_line().rstrip() for i in range(n)]

word_set = set(word)
word = list(word_set)
word.sort()
word.sort( key= len )
for x in word:
    print(x)