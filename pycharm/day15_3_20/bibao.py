def make_average():
    count = 0
    total = 0

    def average(value):
        nonlocal count, total
        count += 1
        total += value
        return total / count

    return average


agv = make_average()
print(agv(10))
print(agv(11))
print(agv(12))
