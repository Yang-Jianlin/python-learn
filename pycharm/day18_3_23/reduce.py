from functools import reduce


def prod(list1):
    return reduce(lambda x, y: x*y, list1)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
