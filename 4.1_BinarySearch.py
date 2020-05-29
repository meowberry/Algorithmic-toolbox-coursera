# python3

s = [int(i) for i in input().split()]
search_s = [int(i) for i in input().split()]

n = s[0]
s = s[1:]


def binary_search(s, elt, r):
    l = 0
    while l <= r:
        m = (l+r)//2
        if elt > s[m]:
            l = m + 1
        elif elt < s[m]:
            r = m - 1
        else:
            return m
    return -1


soln = list()
for i in search_s[1:]:
    ans = binary_search(s, i, n-1)
    soln.append(ans)
print(' '.join([str(i) for i in soln]))
