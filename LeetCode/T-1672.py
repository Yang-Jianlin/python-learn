def maximumWealth(accounts):
    max = 0
    for i in accounts:
        s = 0
        for num in i:
            s = s + num
        if max < s:
            max = s
    return max


if __name__ == '__main__':
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(maximumWealth(accounts))
