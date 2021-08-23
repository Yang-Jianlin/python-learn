def numJewelsInStones(jewels, stones):
    num = 0
    for i in jewels:
        for j in stones:
            if i == j:
                num += 1

    return num


if __name__ == '__main__':
    j = 'z'
    s = 'ZZ'
    print(numJewelsInStones(j, s))
