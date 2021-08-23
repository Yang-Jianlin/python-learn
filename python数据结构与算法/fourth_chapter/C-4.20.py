def sort_num(s, i, j, k):
    if i >= j:
        return s
    else:
        while i < j and s[i] < k:
            i += 1
        while j > i and s[j] > k:
            j -= 1
        s[i], s[j] = s[j], s[i]
        if s[i] == s[j]:
            j -= 1
        return sort_num(s, i, j, k)


if __name__ == '__main__':
    s = [1, 5, 4, 2, 2, 7, 8]
    print(sort_num(s, 0, len(s)-1, 2))
