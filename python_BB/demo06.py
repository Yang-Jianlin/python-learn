def outer(num):
    a = 10

    def inner():
        b = a + num  # 内部函数引用外部变量
        print("内部函数:", b)

    return inner  # 返回值是内部函数


r = outer(5)  # 调用函数，r接收返回值
r()  # 返回值是内部函数，所以r()实质上就是执行inner()
