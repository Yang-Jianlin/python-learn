import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


b = Bus(['Tom', 'Jhon', 'Jane', 'Dail'])
print(b.passengers)
b.pick('Trump')
print(b.passengers)

print('copy test-------')
b2 = copy.copy(b)
b3 = copy.deepcopy(b)
print(b2.passengers)
print(b3.passengers)
b.drop('Tom')
print(b.passengers)
print(b2.passengers)
print(b3.passengers)

