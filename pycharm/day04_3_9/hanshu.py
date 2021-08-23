def print_parm(title, **params):
    print(title)
    print(params)


print_parm("name", x=1, y=2)


def num_sum(*params):
    return zip(params)


para1 = [1, 2, 3]
para2 = [3, 4, 5]
print(list(zip(para1, para2)))
num = num_sum(para1, para2)
print(num)
