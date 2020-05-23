# python3
n = int(input())

if n <= 1:
    print(n)
    quit()


lesser = (n + 2) % 60
if lesser == 1:
    print(0)
    quit()
elif lesser == 0:
    print(9)
    quit()


def fib(n):
    a, b = 0, 1
    for _ in range(2, lesser+1):
        c = a + b
        c = c % 10
        b, a = c, b
    if c != 0:
        print(c-1)
    else:
        print(9)


fib(lesser)