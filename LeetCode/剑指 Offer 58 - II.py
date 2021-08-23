def reverseLeftWords(s: str, n: int):
    slist = list(s)
    for i in range(n):
        slist.append(slist.pop(0))
    return ''.join(slist)


if __name__ == '__main__':
    s = "lrloseumgh"
    print(reverseLeftWords(s, 6))
