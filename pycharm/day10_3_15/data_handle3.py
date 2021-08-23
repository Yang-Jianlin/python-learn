file1 = open('data_handle2.txt', 'r')
file2 = open('data_handle3.txt', 'a')

data = set()
num = 0
while True:
    if file1.readline():
        data.add(file1.readline())
    else:
        break
    num = num + 1

print(num)
print(data)

data_list = list(data)
data_list.sort()
print(data_list)
for d in data_list:
    file2.write(d)
