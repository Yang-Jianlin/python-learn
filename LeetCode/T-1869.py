def checkZeroOnes(str):
    result = {'0': 0, '1': 0}
    max0 = 0
    max1 = 0
    for i in range(len(str)):
        if str[i] == '0':
            j = i+1
            max0 += 1
            if j >= len(str):
                if max0 > result['0']:
                    result['0'] = max0
            elif str[j] != '0':
                if max0 > result['0']:
                    result['0'] = max0
                max0 = 0
        elif str[i] == '1':
            j = i+1
            max1 += 1
            if j >= len(str):
                if max1 > result['1']:
                    result['1'] = max1
            elif str[j] != '1':
                if max1 > result['1']:
                    result['1'] = max1
                max1 = 0

    print(result)
    if result['0'] >= result['1']:
        return False
    else:
        return True


if __name__ == '__main__':
    str = "0111010011"
    print(checkZeroOnes(str))
