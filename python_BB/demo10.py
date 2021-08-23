from user import *


class EnterNet:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def skip(self):
        l = login.Login(self.name, self.passwd)
        if l.login():
            print('Login success')
        else:
            print('Name or password is Error')


if __name__ == '__main__':
    enter = EnterNet('张三', '12345666')
    enter.skip()
