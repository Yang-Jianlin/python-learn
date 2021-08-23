from collections import namedtuple

city = namedtuple('city', 'name country population coordinates')
tokyo = city('Tokyo', 'Jp', '32.233', (35.123213, 168.321423))
print(tokyo.name)
