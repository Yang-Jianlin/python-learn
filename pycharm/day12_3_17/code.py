file1 = open('code.txt', 'a')
str_info = 'abs sfd\n'
file1.write(str_info)
file1.close()


file2 = open('code.txt', 'r')
while True:
    str_du = file2.readline()
    if str_du:
        print(str_du)
    else:
        break
file2.close()
