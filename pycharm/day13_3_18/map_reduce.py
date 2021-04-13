from functools import reduce

list_num = [1, 3, 5, 7, 8]
m = map(lambda x: x * x, list_num)
print(m)
print(list(m))

try:
    r = reduce(lambda x, y: x * y, list_num)
    print(r)
except Exception as info_error:
    print(info_error)
