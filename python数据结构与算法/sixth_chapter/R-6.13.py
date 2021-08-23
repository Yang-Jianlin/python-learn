from collections import deque
from sixth_chapter.queue import ArrayQueue


def sort_dq(D, Q):
    # 先将双端队列的元素写入队列Q中，变为[1,2,3,8,7,6,4,5]
    for i in range(0, len(D)):
        if i < 3:
            Q.enqueue(D.popleft())
        if i > 4:
            Q.enqueue(D.pop())
    Q.enqueue(D.popleft())
    Q.enqueue(D.pop())

    # 接下来将Q元素出队从双端队列的尾部写入变为[1,2,3,8,7,6,4,5]
    while not Q.is_empty():
        D.append(Q.dequeue())

    # 接下来的处理，就是借用队列Q，将[8，7，6，4，5]变为[5，4，6，7，8]
    for j in range(0, 5):
        Q.enqueue(D.pop())

    # 将[5，4，6，7，8]写回双端队列
    while not Q.is_empty():
        D.append(Q.dequeue())


if __name__ == '__main__':
    D = deque()
    Q = ArrayQueue()
    for i in range(1, 9):
        D.append(i)
    print(D)
    sort_dq(D, Q)
    print(D)
