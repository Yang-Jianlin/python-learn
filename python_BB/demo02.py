def add_dict(books):
    book_dict = {}
    flag = 1
    while flag:
        book_dict['书名'] = input("please enter bookName:")
        book_dict['作者'] = input("please enter authorName:")
        book_dict['价格'] = input("please enter priceNum:")
        for i in books:
            if book_dict['书名'] == i['书名']:
                print('book is existed')
                break
        else:
            books.append(book_dict)
            flag = int(input('继续添加(1:是，0：否):'))
    return books


def print_dict(books):
    for i in books:
        print(i)


if __name__ == '__main__':
    books = [{'书名': '百年孤独', '作者': 'jhon', '价格': '56'},
             {'书名': '平凡的世界', '作者': '路遥', '价格': '47'},
             {'书名': '三国演义', '作者': '罗贯中', '价格': '66'}]
    print_dict(add_dict(books))
