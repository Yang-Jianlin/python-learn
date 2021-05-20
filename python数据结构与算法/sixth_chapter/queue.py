"""
基于数组的队列实现
"""


class ArrayQueue:
    # 队列的容量
    CAPACITY = 10

    def __init__(self):
        # 创建一个数组，初始的容量为10
        self.data = [None] * ArrayQueue.CAPACITY
        # size表示队列中存储的当前元素个数，初始化时队列为空，元素个数为0
        # front表示队列的第一个元素的索引，初始化时队列为空，第一个元素应该放在0位置
        self.size = 0
        self.front = 0

    # 返回当前队列的元素个数
    def __len__(self):
        return self.size

    # 若队列为空，返回True
    def is_empty(self):
        if self.size == 0:
            return True
        return False

    # 在不移除元素的前提下(不出队)返回队列的第一个元素
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data[self.front]

    # 出队方法，返回出队的元素
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        # 出队遵循FIFO，取出队头元素，替换为None
        answer = self.data[self.front]
        self.data[self.front] = None
        # 取出第一个元素之后，第二元素变为了第一个，取余操作是解决循环队列问题
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        # 当存储的元素降低到数组总的存储能力的1/4时，将数组的大小缩小到当前容量的一半，
        # 保证队列的健壮性
        if 0 < self.size < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return answer

    # 入队操作，向队尾插入一个元素
    def enqueue(self, e):
        # 当队满时，需要扩充队列的容量，一般就是将当前队列容量变成2倍
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        # 插入的位置(队尾)
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    # 动态的改变队列的存储容量
    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1+walk) % len(old)
        self.front = 0
