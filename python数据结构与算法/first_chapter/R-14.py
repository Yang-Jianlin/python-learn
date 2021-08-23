def pow_num(n):
    return list(map(lambda x: x*x, list(range(1, n+1))))


if __name__ == '__main__':
    print(pow_num(10))
