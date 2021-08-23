def is_event(k):
    # 奇数的二进制最后一位为1，与0001进行与运算后，整体为1
    # 偶数的二进制最后一位为0，与0001进行与运算后，整体为0
    if k & 1:
        return False
    return True


if __name__ == '__main__':
    print(is_event(9))
