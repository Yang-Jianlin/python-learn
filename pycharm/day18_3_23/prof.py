from functools import reduce


def prod(list1):
    s = 1
    n = 0
    while n < len(list1):
        s = s*list1[n]
        n += 1
    return s


print(prod([1, 2, 3, 4]))
