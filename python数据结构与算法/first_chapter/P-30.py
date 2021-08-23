def count_num(num, n):
    if num/2 < 2:
        return n+1
    return count_num(num/2, n+1)  # 必须加上return，不然返回为None


if __name__ == '__main__':
    print(count_num(16, 0))
