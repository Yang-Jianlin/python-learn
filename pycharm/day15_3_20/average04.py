def make_average():
    series = []

    def average(value):
        series.append(value)
        total = sum(series)
        return total/len(series)

    return average


agv = make_average()
print(agv(10))
print(agv(11))
print(agv(12))
