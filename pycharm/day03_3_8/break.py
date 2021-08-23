from math import sqrt
for num in range(99, 82, -1):
    n = sqrt(num)
    print("%5.2f" % n)
    if n == int(n):
        print(num)
        break

else:
    print("don't find")

a = "aa"
if a == "num":
    pass
