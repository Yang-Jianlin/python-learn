def story1(*params):
    print(params)


def story2(*params):
    print("There is a {job}, his name is {name}.".format_map(params[1]))


def story3(**params):
    print(params)


def story4(**params):
    print("There is a {job}, his name is {name}.".format_map(params))


num1 = [1, 2, 3]
info1 = {"name": "Tom", "job": "king"}
info2 = {"name": "Jhon", "job": "teacher"}
info3 = {"age": 16, "address": "beijing"}
story1(*num1)  
story1(info1, info2)
story2(info1, info2)
story3(name="Tom", job="king")
story3(**info1, **info3)
story4(**info1, **info3)
