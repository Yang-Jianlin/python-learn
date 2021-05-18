class ArrayStack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.data[-1]