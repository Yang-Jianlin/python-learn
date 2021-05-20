from sixth_chapter.stack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


if __name__ == '__main__':
    S = ArrayStack()
    T = ArrayStack()
    for i in range(0, 10):
        S.push(i)
    transfer(S, T)
    print(T.data)
