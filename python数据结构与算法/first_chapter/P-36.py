def count(str_list):
    str = str_list.split()
    # key_num = []
    # for i in range(len(str)):
    #     key_num.append(1)
    # str_dict = dict(zip(str, key_num))
    i = 0
    while i < len(str):
        j = 0
        count = 1
        while j < len(str):
            if str[i] == str[j]:
                count += 1
            j += 1
        print('{0} count is {1}'.format(str[i], count-1))
        i += 1


if __name__ == '__main__':
    str='abc bcdef abc shg shg weu'
    count(str)
