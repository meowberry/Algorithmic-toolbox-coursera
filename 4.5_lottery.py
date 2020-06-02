# python3


lst = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    lst.append((a, 'l'))
    lst.append((b, 'r'))

points = input().split()
for i in points:
    lst.append((int(i), 'p'))

lst.sort()

segment_count = 0
point_segment_dict = dict()
for i in lst:
    if i[1] == 'l':
        segment_count += 1
    elif i[1] == 'r':
        segment_count -= 1
    else:
        point_segment_dict[i[0]] = segment_count

temp = ''
for i in points:
    temp += str(point_segment_dict[int(i)]) + ' '
print(temp[:-1])
