# python3


def get_change(money):
    count = 0
    for i in [10, 5, 1]:
        if money >= i:
            t = money // i
            count += t
            money %= i
            if money == 0:
                print(count)


if __name__ == '__main__':
    money = int(input())
    get_change(money)
