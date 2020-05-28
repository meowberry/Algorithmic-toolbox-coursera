# python3

n = int(input())
lst = [int(i) for i in input().split()]


def BiggerOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit)) >= int(str(max_digit)+str(digit))


def LargestNumber(lst):
    answer = []

    while lst != []:
        max_digit = 0
        for digit in lst:
            if BiggerOrEqual(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


print(''.join([str(i) for i in LargestNumber(lst)]))
