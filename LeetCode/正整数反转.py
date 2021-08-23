def reversenum(num):
    print(num % 10, end='')
    if num > 10:
        reversenum(num // 10)


if __name__ == '__main__':
    num = 12345
    reversenum(num)
