registry = []


def register(func):
    print('running register({0})'.format(func))
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


print('running main()')
print('registry ->', registry)
