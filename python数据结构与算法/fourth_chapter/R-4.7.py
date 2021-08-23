from math import pow


def str_int(s, index, num):
    if index < 0:
        return int(num)
    else:
        num = num + int(s[index]) * (1 * pow(10, len(s)-index-1))
        return str_int(s, index-1, num)


if __name__ == '__main__':
    s = '3457384'
    print(str_int(s, len(s)-1, 0))
