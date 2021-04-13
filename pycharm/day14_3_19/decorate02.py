registry = []


def register(func):
    print("running register ({0})".format(func))
    registry.append(func)
    return func


@register
def fun1():
    print("running fun1!")


@register
def fun2():
    print("running fun2!")


def fun3():
    print("running fun3!")


def main():
    print("running main()!")
    print("running register({0})".format(registry))
    fun1()
    fun2()
    fun3()


if __name__ == '__main__':
    main()
