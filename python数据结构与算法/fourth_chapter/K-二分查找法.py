def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mod = (low + high) // 2
        mod_num = data[mod]
        if target == mod_num:
            return True
        elif target < mod_num:
            return binary_search(data, target, low, mod-1)
        else:
            return binary_search(data, target, mod+1, high)


if __name__ == '__main__':
    data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    print(binary_search(data, 21, 0, len(data)-1))
