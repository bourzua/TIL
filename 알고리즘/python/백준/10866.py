import sys

N = int(sys.stdin.readline())
deck = []

for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        deck.insert(0, cmd[1])
    elif cmd[0] == 'push_back':
        deck.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(0))
    elif cmd[0] == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop(-1))
    elif cmd[0] == 'size':
        print(len(deck))
    elif cmd[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    else:
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])