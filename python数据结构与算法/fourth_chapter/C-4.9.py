def best_num(s, index):
    if index == len(s) - 1:
        return s[index], s[index]
    max, min = best_num(s, index + 1)
    if min < s[index] and max < s[index]:
        return min, s[index]
    elif min < s[index] < max:
        return min, max
    else:
        return s[index], max


if __name__ == '__main__':
    s = [1, 85, 6, 54, 12]
    print(best_num(s, 0))
