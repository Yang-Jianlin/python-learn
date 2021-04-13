import bisect

a = [1, 5, 12, 3, 6, 9]
b = [0, 2, 5, 5]
a.sort()
for needle in b:
    position = bisect(a, needle)
print(a)
