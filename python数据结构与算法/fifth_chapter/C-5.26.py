def repeat_num(b, n):
    num = {}
    for i in range(0, len(b)):
        total = 1
        j = i+1
        for j in range(j, len(b)):
            if b[i] == b[j]:
                total = total + 1
        num[str(b[i])] = total
        if total == n:
            break

    return num


if __name__ == '__main__':
    b = [1, 5, 6, 5, 5, 5, 5]
    print(repeat_num(b, 5))
