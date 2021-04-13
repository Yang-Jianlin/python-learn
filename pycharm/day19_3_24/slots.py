from types import MethodType


class Student:
    pass


s = Student()


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.set_age)
