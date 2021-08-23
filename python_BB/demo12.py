import re

str1 = 'I am is str'
print(re.sub('str', 'as', str1))

str2 = 'I am is yang, and:are you Li'
print(re.split(r'[,:]', str2))
print(str2.split(' '))
