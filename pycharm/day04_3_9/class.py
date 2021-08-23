class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __fun(self):
        print("asdufhu")

    def greet(self):
        print("Hello, {0}!".format(self.name))
        self.__fun()


foo = Person()
foo.set_name("Tom")
print(foo.get_name())
foo.greet()
