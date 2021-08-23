def func(name='111'):
    def f1():
        print('running f1()!')

    def f2():
        print('running f2()!')

    if name == '111':
        return f1
    else:
        return f2()


print(func('111'))
# print(func('222'))
func('222')
