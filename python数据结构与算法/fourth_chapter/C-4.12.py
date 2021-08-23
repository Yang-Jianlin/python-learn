def mul_num(m, n, mul):
    if n == 1:
        return mul
    else:
        mul = mul + m
        return mul_num(m, n-1, mul)


if __name__ == '__main__':
    m = 3
    n = 1
    mul = m
    print(mul_num(m, n, mul))
