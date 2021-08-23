class Foo:
    def __getitem__(self, item):
        return range(0, 30, 5)[item]


f = Foo()
print(f[2])
