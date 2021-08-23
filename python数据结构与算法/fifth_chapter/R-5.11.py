def array_sum(arr, n):
    total = 0
    for i in range(0, n):
        for j in range(0, n):
            total = total + arr[i][j]

    return total


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(array_sum(arr, 3))
