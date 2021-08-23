def odd_num(s, i, j):
    if i >= j:
        return s
    else:
        while i < j and s[i] % 2 == 0:
            i += 1
        while j > i and s[j] % 2 != 0:
            j -= 1
        s[i], s[j] = s[j], s[i]
        return odd_num(s, i+1, j-1)


if __name__ == '__main__':
    s = [6, 5, 2, 4, 7, 8]
    print(odd_num(s, 0, len(s)-1))
