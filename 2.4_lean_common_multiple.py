# python3
a, b = [int(i) for i in input().split()]


def evclid_gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return evclid_gcd(b, c)


if a > b:
    gcd = evclid_gcd(a, b)
else:
    gcd = evclid_gcd(b, a)

print(a*b//gcd)
