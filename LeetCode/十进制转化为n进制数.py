def func(num, n):
    apl = ['A', 'B', 'C', 'D', 'E', 'F']
    res = []
    if num < n:
        return num
    while num >= n:
        num1 = num % n
        num2 = num // n
        num = num2
        if num1 >= 10:
            res.append(apl[num1 % 10])
        else:
            res.append(str(num1))
    if num >= 10:
        res.append(apl[num % 10])
    else:
        res.append(str(num))
    res = res[::-1]
    return ''.join(res)


if __name__ == '__main__':
    num = 175
    n = 16
    print(func(num, n))
