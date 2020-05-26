# python3

n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()

win = n
prizes = []
for i in range(1, n):
    if win > 2*i:
        prizes.append(i)
        win -= 1
    else:
        prizes.append(win)
        break
print(len(prizes))
print(' '.join([str(i) for i in prizes]))
