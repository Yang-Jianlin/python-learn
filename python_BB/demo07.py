import os


# file = open('file.txt', 'r')
# a = ['as', 'ds', 'ds']
#
# result = file.readable()
# if result:
#     container = file.read()
#     print(container)
# else:
#     print('file can\'t read')

path = os.path.dirname(__file__)
print(path)
path_end = os.path.join(path, 'file2.txt')
print(path_end)

with open('file.txt', 'r') as file:
    result = file.read()
    with open(path_end, 'w') as file2:
        file2.write(result)

str1 = 'xcds,cdj,sdiwe'
print(str1.split(','))
