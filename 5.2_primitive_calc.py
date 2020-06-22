# python3
import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
numOperations = [0, 0] + [math.inf]*(n-1)

for i in range(2, n+1):
    temp1, temp2, temp3 = [math.inf]*3

    temp1 = numOperations[i-1] + 1
    if i % 2 == 0:
        temp2 = numOperations[i//2] + 1
    if i % 3 == 0:
        temp3 = numOperations[i//3] + 1
    min_ops = min(temp1, temp2, temp3)
    numOperations[i] = min_ops

print(numOperations[n])

nums = [n]
while n != 1:
    if n % 3 == 0 and numOperations[n]-1 == numOperations[n//3]:
        nums += [n//3]
        n = n//3
    elif n % 2 == 0 and numOperations[n]-1 == numOperations[n//2]:
        nums += [n//2]
        n = n//2
    else:
        nums += [n-1]
        n = n - 1

print(' '.join([str(i) for i in nums][::-1]))
