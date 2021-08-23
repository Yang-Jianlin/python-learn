while True:
    try:
        x = int(input("please enter first number:"))
        y = int(input("please enter second number:"))
        print(x / y)
    except Exception as e:
        print("input invalid! ", e)
        print("try again!")
    else:
        break
