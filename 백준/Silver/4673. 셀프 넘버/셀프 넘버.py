all_nums = set(range(1, 10001))
generated = set()

for i in range(1, 10001):
    total = i + sum(int(d) for d in str(i))
    generated.add(total)

self_numbers = sorted(all_nums - generated)

for num in self_numbers:
    print(num)