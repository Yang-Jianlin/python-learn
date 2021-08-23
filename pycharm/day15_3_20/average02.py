class Average:
    def __init__(self, *series_num):
        self.series_num = list(series_num)

    def agv_num(self, *args, **kwargs):
        print(self.series_num)
        total = sum(self.series_num)
        return total/len(self.series_num)


agv = Average(10, 11, 12)
print(agv.agv_num())
