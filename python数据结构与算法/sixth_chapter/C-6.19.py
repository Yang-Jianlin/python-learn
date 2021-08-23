from sixth_chapter.stack import ArrayStack


def is_matched(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            e = S.pop()
            if tag[1:] != e[:len(tag) - 1]:
                return False
        j = raw.find('<', k + 1)
    return S.is_empty()


if __name__ == '__main__':
    print(is_matched('<name attribute="seda"></name>'))
