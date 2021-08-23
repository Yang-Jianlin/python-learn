class ArrayStack:
    CAPACITY = 10

    def __init__(self):
        # 创建一个数组，初始的容量为10
        self.data = [None] * ArrayStack.CAPACITY
        self.size = 0
        self.top = -1

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        self.size -= 1
        return answer

    def push(self, e):
        self.top += 1
        self.data[self.top] = e
        self.size += 1


if __name__ == '__main__':
    S = ArrayStack()

    for i in range(0, 10):
        S.push(i)
    print(S.data)

    for j in range(0, 3):
        print(S.pop(), end=' ')
    print()

    print(S.data)
    S.push(10)
    print(S.data)
