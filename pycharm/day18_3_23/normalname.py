def normalize(name):
    return name.capitalize()


l2 = list(map(normalize, ['adam', 'LISA', 'barT']))
print(l2)
