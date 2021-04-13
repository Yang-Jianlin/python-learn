d = {
    'x': 'A',
    'y': 'B',
    'z': 'C'
}

for x, v in d.items():
    print(x + '=' + v)

print('------------------------------')

L = ['Hello', 123, 'World', '12', 'Apple']
s = [s.lower() for s in L if isinstance(s, str)]
print(s)
