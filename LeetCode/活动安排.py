def activity(time):
    time = sorted(time, key=lambda x: x[1])
    if len(time) == 1:
        return time
    re = [time[0]]
    i = 0
    j = 1
    while i < len(time) - 1:
        if time[j][0] >= time[i][1]:
            re.append(time[j])
            i = j
        j += 1
        if j > len(time) - 1:
            break
    return re, len(re)


if __name__ == '__main__':
    time = [(10, 12), (12, 14), (10, 15), (17, 18), (18, 20), (21, 23), (22, 23)]
    re, n = activity(time)
    print(re)
    print(n)
