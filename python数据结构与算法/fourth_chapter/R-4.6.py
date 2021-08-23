def harm_num(n, sum):
    if n == 0:
        return sum
    else:
        sum = sum + 1/n
        return harm_num(n-1, sum)


if __name__ == '__main__':
    print(harm_num(3, 0))
