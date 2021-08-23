def story1(**kwds):
    print("There is a {job}, his name is {name}.".format_map(kwds))


def story2(*kwds):
    print("There is a {job}, his name is {name}.".format_map(kwds[1]))


def story3(**kwds):
    print(kwds)
    # print("There is a {job}, his name is {name}.".format_map(kwds))


info1 = {"name": "Tom", "job": "king"}
info2 = {"name": "Jhon", "job": "teacher"}
info3 = {"age": 16, "address": "beijing"}
story1(name="Tom", job="king")
story1(**info1)
story2(info1, info2)
story2(*(1, 2, 3))
story3(**info1, **info3)
