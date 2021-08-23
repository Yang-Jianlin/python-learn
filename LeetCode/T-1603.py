class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        bool_list = []
        if carType == 1:
            self.big -= 1
            if self.big < 0:
                bool_list.append(False)
            else:
                bool_list.append(True)
        elif carType == 2:
            self.medium -= 1
            if self.medium < 0:
                bool_list.append(False)
            else:
                bool_list.append(True)
        elif carType == 3:
            self.small -= 1
            if self.small < 0:
                bool_list.append(False)
            else:
                bool_list.append(True)
        return bool_list


if __name__ == '__main__':
    p = ParkingSystem(1, 1, 0)
    print(p.addCar(1))
    print(p.addCar(2))
    print(p.addCar(3))
    print(p.addCar(1))
