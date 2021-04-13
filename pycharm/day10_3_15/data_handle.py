file_data = open('data.txt', 'r')
file_handle = open('data_handle1.txt', 'a')

'''num = []
while True:
    if file_data.readline():
        num.append(len(file_data.readline()))
    else:
        break

num.sort()
print(num)'''

while True:
    if file_data.readline():
        if len(file_data.readline()) > 100:
            file_handle.write(file_data.readline())
    else:
        break
