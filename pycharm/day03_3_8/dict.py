user = {
    "Tom": {
        "Num": "185365",
        "Adr": "Beijing"
    },
    "Jane": {
        "Num": "458894",
        "Adr": "Zhengzhou"
    },
    "Jhon": {
        "Num": "485498",
        "Adr": "Shanghai"
    }
}

user_name = input("Please enter name:")
if user_name in user:
    print("{0}'s address is {1}".format(user_name, user[user_name]["Adr"]))
    print("{0}'s Number is {1}".format(user_name, user[user_name]["Num"]))
