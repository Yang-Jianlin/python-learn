def max_num(s, index):
    if index == len(s)-1:
        return s[index]
    max = max_num(s, index+1)
    if max > s[index]:
        return max
    else:
        return s[index]


if __name__ == '__main__':
    s = [1, 85, 6, 54, 12]
    print(max_num(s, 0))
