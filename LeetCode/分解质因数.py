def split_num(num):
    result = []
    while num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                num //= i
                result.append(i)
                break
    return result


if __name__ == '__main__':
    num = 100
    print(split_num(num))
