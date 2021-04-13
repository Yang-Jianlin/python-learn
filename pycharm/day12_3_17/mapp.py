from types import MappingProxyType
d = {'1': 12, '2': 23}
d_pox = MappingProxyType(d)
print(d_pox)
print(d)
print(d_pox['1'])
try:
    d['1'] = 123
     
except Exception as info:
    print(info)
print(d_pox)
print(d)
print(d_pox['1'])
