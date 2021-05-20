class ArrayStack:

    # 初始化一个空列表
    def __init__(self, maxlen):
        self.data = []
        self.maxlen = maxlen

    # 返回栈的大小
    def __len__(self):
        return len(self.data)

    # 若栈为空，返回True
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    # 入栈操作
    def push(self, e):
        if self.__len__() >= self.maxlen:
            raise Exception('stack is full')
        self.data.append(e)

    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.data.pop()

    # 在不删除元素(不出栈)的前提下，返回栈顶元素
    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.data[-1]


if __name__ == '__main__':
    stack = ArrayStack(3)
    for i in range(0, 4):
        stack.push(i)
    print(stack.data)
