def change(count, value, money):
    re = 0
    for i in range(len(value) - 1, -1, -1):
        num = min(money // value[i], count[i])
        money -= num * value[i]
        re += num
    if money > 0:
        re = -1
    return re


if __name__ == '__main__':
    count = [3, 0, 2, 1, 0, 3, 5]
    value = [1, 2, 5, 10, 20, 50, 100]
    money = 358
    print(change(count, value, money))
