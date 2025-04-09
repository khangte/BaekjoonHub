import sys
readline = sys.stdin.readline

n = int(readline().rstrip())

stack = []
for _ in range(n):
    cmd = list(map(str, readline().rstrip().split()))

    if cmd[0] == 'push':
        cmd[1] = int(cmd[1])
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else: print(-1)
