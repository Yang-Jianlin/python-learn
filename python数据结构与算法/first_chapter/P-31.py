def find_money(pay, put):
    coins = {'0.1': 0, '0.5': 0, '1': 0, '5': 0,
             '10': 0, '20': 0, '50': 0, '100': 0}
    balance = put - pay
    coins['100'] = int(balance / 100)
    balance = balance % 100
    coins['50'] = int(balance / 50)
    balance = balance % 50
    coins['20'] = int(balance / 20)
    balance = balance % 20
    coins['10'] = int(balance / 10)
    balance = balance % 10
    coins['5'] = int(balance / 10)
    balance = balance % 5
    coins['1'] = int(balance / 1)
    balance = balance % 1
    coins['0.5'] = int(balance / 0.5)
    balance = balance % 0.5
    coins['0.1'] = int(balance / 0.1)
    return coins


if __name__ == '__main__':
    print(find_money(10, 34.5))
