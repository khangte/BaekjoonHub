n = int(input())

def fibo(num):
    a, b = 0, 1
    if num == 0:
        return 0
    elif num == 1:
        return 1

    for _ in range(num):
        a, b = b, a+b

    return a

print(fibo(n))

