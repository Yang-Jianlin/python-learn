database = [
    ["Jhon", "123456"],
    ["Tom", "789456"],
    ["Jane", "852657"]
]

username = input("please enter name:")
userpwd = input("please enter passwd:")

if [username, userpwd] in database:
    print("Access!")
