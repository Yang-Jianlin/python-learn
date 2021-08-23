file1 = open('data_handle1.txt', 'r')
file2 = open('data_handle2.txt', 'a')

while True:
    if file1.readline():
        try:
            str = file1.readline()
            num_start = str.index('IP 10')
            num_end = str.index(': Flag')
            print(str[num_start:num_end])
            file2.write(str[num_start:num_end]+'\n')
        except Exception:
            pass
    else:
        break
