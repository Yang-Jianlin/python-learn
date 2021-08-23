def decode(encoded, first):
    origin = [first, ]
    j = 0
    for i in encoded:
        origin.append(i ^ origin[j])
        j += 1
    return origin


if __name__ == '__main__':
    encoded = [6, 2, 7, 3]
    print(decode(encoded, 4))
