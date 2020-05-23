# python3
m, n = [int(i) for i in input().split()]

if n <= 1:
    print(n)
    quit()


lesser_n = (n+2) % 60
lesser_m = (m+1) % 60


def fib(n):
    a, b = 0, 1
    for i in range(2, n+1):
        c = a+b
        c = c % 10
        b, a = c, b
    return (c-1)


if lesser_n <= 1:
    a = lesser_n-1
else:
    a = fib(lesser_n)

if lesser_m <= 1:
    b = lesser_m-1
else:
    b = fib(lesser_m)

if a >= b:
    print(a-b)
else:
    print(10+a-b)
