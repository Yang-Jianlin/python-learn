from random import randrange
import operator


def random_list(l):
    for i in reversed(range(0, len(l))):
        j = randrange(i + 1)
        l[i], l[j] = l[j], l[i]

    return l


def probability(ll):
    l_dict = {}
    for i in range(0, len(ll)):
        total = 1
        for j in range(0, len(ll)):
            if operator.eq(ll[i], ll[j]):
                total = total + 1
        l_dict[str(ll[i])] = total-1

    return l_dict


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ll = []
    i = 0
    while i < 20000:
        a = random_list(l)
        ll.extend(a)
        i += 1
    li = [ll[x:x + 4] for x in range(0, len(ll), 4)]
    di = probability(li)
    for key in di:
        p = di[key] / sum(di.values())
        print('%.3f' % p, end=', ')
