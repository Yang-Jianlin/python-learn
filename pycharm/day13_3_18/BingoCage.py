import random


class BingoCage:
    def __init__(self, lst_range):
        self.__lst_range = list(lst_range)
        print(self.__lst_range)
        random.shuffle(self.__lst_range)
        print(self.__lst_range)

    def pick(self):
        try:
            return self.__lst_range.pop()
        except Exception as info_error:
            print(info_error)

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(4))
print(bingo.pick())
print(callable(bingo))
