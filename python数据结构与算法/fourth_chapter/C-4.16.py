def reserve(s, start, end):
    if start >= end:
        return ''.join(s)
    else:
        s[start], s[end] = s[end], s[start]
        return reserve(s, start+1, end-1)


if __name__ == '__main__':
    s = 'asdh$ssy'
    print(reserve(list(s), 0, len(s)-1))
