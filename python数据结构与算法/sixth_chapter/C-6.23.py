from sixth_chapter.stack import ArrayStack


def move_num(R, S, T):
    l = S.__len__() + T.__len__()
    while not S.is_empty():
        R.push(S.pop())
    while not T.is_empty():
        R.push(T.pop())
    for i in range(0, 6):
        S.push(R.pop())


if __name__ == '__main__':
    R = ArrayStack()
    S = ArrayStack()
    T = ArrayStack()
    for i in range(1, 10):
        if i < 4:
            R.push(i)
        elif i < 6:
            S.push(i)
        else:
            T.push(i)

    move_num(R, S, T)

    while not R.is_empty():
        print(R.pop(), end=' ')
    print()
    while not S.is_empty():
        print(S.pop(), end=' ')
    print()
    while not T.is_empty():
        print(T.pop(), end=' ')
    print()
