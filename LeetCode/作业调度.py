def work(time, m):
    time = sorted(time, reverse=True)
    if m >= len(time):
        return time[0]
    else:
        tmp = time[:m]
        for i in time[m:]:
            ind = tmp.index(min(tmp))
            tmp[ind] += i
    return max(tmp)


if __name__ == '__main__':
    time = [30, 26, 10, 35, 20, 18, 2, 7]
    m = 3
    print(work(time, m))
