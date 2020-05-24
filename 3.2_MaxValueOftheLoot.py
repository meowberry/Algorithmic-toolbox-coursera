# python3
n, WEI = [int(i) for i in input().split()]
lst = []

if WEI == 0:
    print(0)
    quit()

for _ in range(n):
    val, wei = [int(i) for i in input().split()]
    if val == 0:
        continue
    lst.append((val, wei))

lst.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0

for val, wei in lst:
    if WEI == 0:
        print(total_value)
        quit()
    amt = min(wei, WEI)
    total_value += amt*val/wei
    WEI -= amt

print(total_value)
