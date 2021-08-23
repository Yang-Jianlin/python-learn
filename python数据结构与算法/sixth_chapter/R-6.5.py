from sixth_chapter.stack import ArrayStack


def reserve(S, L):
    for i in L:
        S.push(i)
    for j in range(0, len(L)):
        L[j] = S.pop()


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    S = ArrayStack()
    reserve(S, L)
    print(L)
