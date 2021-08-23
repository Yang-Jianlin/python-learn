from sixth_chapter.stack import ArrayStack


def is_matched(expr):
    lefty = '([{'
    righty = ')]}'
    S = ArrayStack()

    for e in expr:
        if e in lefty:
            S.push(e)
        elif e in righty:
            if S.is_empty():
                return False
            if righty.index(e) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == '__main__':
    expr = '(4+5)'
    print(is_matched(expr))
