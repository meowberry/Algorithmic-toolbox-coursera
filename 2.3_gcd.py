# Python3

a, b = [int(i) for i in input().split()]


def evclid_gcd(a, b):
    if b == 0:
        print(a)
        quit()
    c = a % b
    evclid_gcd(b, c)


if a > b:
    evclid_gcd(a, b)
else:
    evclid_gcd(b, a)
