import shelve


def store(database):
    uid = input("please enter id:")
    person = {}
    person['name'] = input("please enter name:")
    person['age'] = input("please enter age:")
    person['phone_number'] = input("please enter phone number:")
    database['uid'] = person


def lookup(database):
    uid = input("please enter the uid:")
    info = input("please enter info:(name,age,phone_number)")
    look_info = info.strip().lower()
    print(look_info.capitalize() + ':', database[uid][look_info])


def print_help():
    print("The available commands are:")
    print("store: Stores information about a person")
    print("lookup: Looks up a person from ID number")
    print("quit: Save changes and exit")
    print("?: Prints this message")


def cmd():
    cmd = input("please enter the command (? for help):")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('E:\\pycharm\day06_3_11\data.dat')
    try:
        while True:
            main_cmd = cmd()
            if main_cmd == 'store':
                store(database)
            elif main_cmd == 'lookup':
                lookup(database)
            elif main_cmd == '?':
                print_help()
            elif main_cmd == 'quit':
                exit()
    except Exception as e:
        print(e)
    finally:
        database.close()


if __name__ == '__main__':
    main()
