def minmax(data):
    max_num = min_num = data[0]
    for n in data:
        if n > max_num:
            max_num = n
        if n <= min_num:
            min_num = n

    return max_num, min_num


if __name__ == '__main__':
    num = [1, 5, 10, 8, 9]
    print(minmax(num))
