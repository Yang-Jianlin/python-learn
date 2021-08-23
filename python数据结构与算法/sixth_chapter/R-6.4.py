from sixth_chapter.stack import ArrayStack


def remove_stack(S):
    if S.is_empty():
        print('删除完成')
    else:
        S.pop()
        remove_stack(S)


if __name__ == '__main__':
    S = ArrayStack()
    for i in range(0, 10):
        S.push(i)
    print(S.data)
    remove_stack(S)
