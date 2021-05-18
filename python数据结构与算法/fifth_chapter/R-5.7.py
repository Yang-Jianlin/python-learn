def find_double(a, n):
    for i in range(0, n):
        j = i + 1
        for j in range(j, n):
            if a[i] == a[j]:
                print(a[i])
                break


if __name__ == '__main__':
    a = [1, 1, 5, 4, 9, 10]
    find_double(a, 6)
