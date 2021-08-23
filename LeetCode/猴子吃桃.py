def monkey(n):
    if n == 1:
        return 1
    else:
        return (monkey(n-1) + 1) * 2


if __name__ == '__main__':
    print(monkey(4))
