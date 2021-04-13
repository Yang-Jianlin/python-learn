class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Ahhaa")
            self.hungry = False
        else:
            print("No, think you!")


class AngleBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squak'

    def sing(self):
        print(self.sound)
        self.hungry = True


b = AngleBird()
b.eat()
b.eat()
b.sing()
b.eat()
