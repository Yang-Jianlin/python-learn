fibs = [0, 1]
n = input("please enter your num:")

for i in range(0, int(n)):
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)
