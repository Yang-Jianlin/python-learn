from time import *
from random import *

data1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(data1)
data2 = (2020, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(data2)

random_time = uniform(time1, time2)
print(asctime(localtime(random_time)))
