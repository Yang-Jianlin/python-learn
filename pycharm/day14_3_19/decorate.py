def deco(fu):
    def fun():
        print("running fun!!!")

    return fu


@deco
def target():
    print("running target!!!")


target()
print(target)
