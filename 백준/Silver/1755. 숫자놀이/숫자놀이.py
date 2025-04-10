m, n = map(int, input().rstrip().split())

num_dict = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
}

result = []
for num in range(m, n+1):
    if (num//10) > 0 :
        num_str = ' '.join([num_dict[num//10], num_dict[num%10]])

    else:
        num_str = num_dict[num]
    
    result.append([num, num_str])

result_sorted = sorted(result, key=lambda x:x[1])

for i in range(len(result_sorted)):
    if i%10 == 0 and i != 0:
        print()
    print(result_sorted[i][0], end=' ')
