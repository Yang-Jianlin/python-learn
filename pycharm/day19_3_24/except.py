def func():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except Exception as error_info:
        print('error information:', error_info)
    finally:
        print('end')

    print('11111')


func()
