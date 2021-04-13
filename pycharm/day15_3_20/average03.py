class Average:
    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        total = sum(self.series)
        return total/len(self.series)


agv = Average()
print(agv(10))
print(agv(11))
print(agv(12))
