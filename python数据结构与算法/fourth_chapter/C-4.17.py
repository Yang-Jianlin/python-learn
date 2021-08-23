def reserve(s, start, end, n):
    if start >= end:
        if n >= len(s) // 2:
            return True
        else:
            return False
    else:
        if s[start] == s[end]:
            n += 1
        return reserve(s, start+1, end-1, n)


if __name__ == '__main__':
    s = 'abcfcba'
    print(reserve(list(s), 0, len(s)-1, 0))
