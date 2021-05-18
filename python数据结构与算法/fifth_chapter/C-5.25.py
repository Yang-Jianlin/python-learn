def remove_all(data, value):
    for i in data:
        if i == value:
            data.remove(i)

    return data


if __name__ == '__main__':
    data = [1, 2, 3, 2, 4, 6, 2]
    print(remove_all(data, 2))
