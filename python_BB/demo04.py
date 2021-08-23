import time
import random


# 简单的装饰器
def decorater(func):
    def wrapped(*args, **kwargs):  # 参数是为了应对各种带参或不带参的函数作为参数传入
        start = time.time()
        func(*args, **kwargs)
        print('刷白墙')
        print('铺地板')
        print('买家具')
        time.sleep(random.randint(1, 5))
        print('装修结束')
        end = time.time()
        print('装修花费的时间：', end-start)
    return wrapped


# 装饰有返回值的函数的装饰器
def decorater1(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)  # 原函数带有返回值，这儿需要变量进行接收
        print('预计装修花费：{}'.format(r))
        print('刷白墙')
        print('铺地板')
        print('买家具')
        time.sleep(random.randint(1, 5))
        print('装修结束')
        end = time.time()
        print('装修花费的时间：', end-start)
        return r+10000
    return wrapped


'''
原函数home()，开始并未装修，但是未来遵循开放封闭原则，不对原函数进行更改，
就用装饰器进行修改装修，装饰器实质上就将home()作为参数传入进去，
然后就可以对原函数内容进行各种添加和修改
也就相当于：home = decorater(home)，由于decorater中的返回值是wrapped，
所以，执行完毕后，home实质上也就是wrapped()了
'''


@decorater
def home():
    print('买了一套房，没装修')


@decorater
def school(address, area):
    print('学校位于：{0}，面积是：{1}'.format(address, area))


@decorater
def hotel(name, address, area):
    print('酒店叫：{0}, 酒店位于：{1}，面积是：{2}'.format(name, address, area))


@decorater1
def factory(name, address, area):
    print('工厂叫：{0}, 工厂位于：{1}，面积是：{2}'.format(name, address, area))
    return 50000


if __name__ == '__main__':
    home()
    print('-----------')
    school('北京', '1200')
    print('-----------')
    hotel(name='锦江之星', address='上海', area='1500')
    print('-----------')
    r = factory(name='苹果', address='加利福尼亚', area='150000')
    print('实际装修花费：{}'.format(r))
