# python3

""" 
Task: Count the number of inversions of a given sequenc
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers
"""


def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]

    return final, inversion_counter


def mergesort(arr):
    global total_count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    total_count += temp

    return sorted_arr


total_count = 0
n = int(input())
seq = [int(i) for i in input().split()]
mergesort(seq)
print(total_count)
