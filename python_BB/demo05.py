a = [['aa', 10], ['bb', 19], ['cc', 9]]


def func(a):
    for i in a:
        return i[1]


# a = sorted(a, key=lambda x: x[1])
# print(a)

c = sorted(a, key=func(a))
print(c)
