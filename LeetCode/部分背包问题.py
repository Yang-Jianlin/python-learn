def bag(matrix, m):
    matrix = sorted(matrix, key=lambda x: x[1] / x[0], reverse=True)
    re = 0
    re_list = [0 for _ in range(len(matrix))]
    n = 0
    for i in matrix:
        if m >= i[0]:
            m -= i[0]
            re += i[1]
            re_list[n] = 1
        elif m > 0:
            re += float(m / i[0] * i[1])
            re_list[n] = float(m / i[0])
            m -= m
        else:
            break
        n += 1

    return matrix, re_list, re


if __name__ == '__main__':
    matrix = [(10, 3), (260, 1000), (40, 10), (120, 50)]
    m = 150
    mat, rel, re = bag(matrix, m)
    print(mat)
    print(rel)
    print(re)
