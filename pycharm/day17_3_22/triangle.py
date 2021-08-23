def triangles(num):
    L = [1]
    m = 0
    while m < num:
        yield L[:]
        L.append(0)
        L = [L[m] + L[m - 1] for m in range(len(L))]
        m += 1


t = triangles(5)
for n in t:
    print(n)
