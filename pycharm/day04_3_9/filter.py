class Filter:
    def init(self):
        self.block = []

    def filter(self, seq):
        for x in seq:
            if x in self.block:
                del seq[seq.index(x)]
        return seq

    '''def filter(self, seq):
        return [x for x in seq if x not in self.block]'''


class SPAMFilter(Filter):
    def init(self):
        self.block = ["SPAM"]


fun = SPAMFilter()
fun.init()
print(fun.filter(["aa", "SPAM", "bb"]))
