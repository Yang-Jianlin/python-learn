class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set(self, *size):
        self.width, self.height = size

    def get(self):
        return self.width, self.height


rec = Rectangle()
rec.set(1, 2)
print(rec.get())
print(rec.width)
