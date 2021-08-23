def fun(s, con, index, n):
    if index > len(s)-1:
        if n > len(s) // 2:
            return True
        else:
            return False
    else:
        if s[index] in con:
            n += 1
        return fun(s, con, index+1, n)


if __name__ == '__main__':
    con = ['a', 'e', 'i', 'o', 'u']
    s = 'h'
    print(fun(s, con, 0, 0))
