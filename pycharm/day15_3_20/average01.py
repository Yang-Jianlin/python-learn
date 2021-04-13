series = []


class Average:
    def __init__(self, series_num):
        self.series_num = series_num

    def __call__(self, *args, **kwargs):
        series.append(self.series_num)
        total = sum(series)
        return total/len(series)


agv = Average(10)
print(agv)
