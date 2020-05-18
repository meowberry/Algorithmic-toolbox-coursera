#python3

n = int(input())

if n <= 1:
    print(n)
    quit()

def fib(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        a, b = b, c 
    print(c)

fib(n)