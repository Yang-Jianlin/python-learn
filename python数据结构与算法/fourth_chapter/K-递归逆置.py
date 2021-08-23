def reverse(data, start, end):
    if start < end - 1:
        data[start], data[end-1] = data[end-1], data[start]
        reverse(data, start+1, end-1)

    return data


if __name__ == '__main__':
    data = [0, 1, 2, 3, 4]
    print(reverse(data, 0, len(data)))
