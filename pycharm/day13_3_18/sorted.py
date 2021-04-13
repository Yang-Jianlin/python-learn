def reverse(word):
    return word[::-1]


fruits = ['sahgyberry', 'zuhua', 'swwberry', 'apple', 'saghsa', 'berry']

# fruits.sort()
fruits2 = sorted(fruits, key=len)
fruits3 = sorted(fruits, key=reverse)
print(fruits)
print(fruits2)
print(fruits3)

print("lamdba 函数的作用")
fruits4 = sorted(fruits, key=lambda word: word[::-1])
print(fruits4)

