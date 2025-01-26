import sys
read_line = sys.stdin.readline

word = read_line().strip().upper()
word_list = list(set(word))

cnt = []
for c in word_list:
    cnt.append(word.count(c))

if cnt.count(max(cnt)) >1:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])