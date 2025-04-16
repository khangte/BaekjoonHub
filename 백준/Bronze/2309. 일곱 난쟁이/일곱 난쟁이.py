from itertools import combinations

data = set()
for _ in range(9):
    data.add(int(input().rstrip()))

dwarf = list(combinations(data, 7))

for d in dwarf:
    if sum(d) == 100:
        result = list(d)
        result.sort()
        break

for datum in result:
    print(datum)