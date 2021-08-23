from python_BB.user import userdb


class Login:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def login(self):
        if self.name in userdb.user_info:
            if self.passwd == userdb.user_info[self.name]:
                return True
            else:
                return False
        else:
            return False


# if __name__ == '__main__':
#     l = Login('李四', '234567')
#     print(l.login())
