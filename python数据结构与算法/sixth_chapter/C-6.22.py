from sixth_chapter.stack import ArrayStack

"""
后缀表达式的转换
用两个栈来实现，一个栈存储运算数，一个栈存储运算符
从左到右遍历输入的中缀表达式：
1、如果是操作数的话，直接压入存放操作数的堆栈；
2、如果是"("左括号的话，直接压入存放运算符的堆栈；
3、如果是")"右括号的话，就从运算符堆栈中弹数据，并将弹出的数据压入到操作数堆栈中，直到遇到"("为止，
    需要注意的是，"("是必须要从运算符堆栈中弹出的，但是不压入到操作数堆栈，后缀表达式中是不包含括号的；
4、如果是其他符号，就是其他的运算符+-*/这些，那么就：
    a、如果运算符堆栈为空，则直接压入运算符堆栈；
    b、如果不为空且此时运算符堆栈的栈顶元素为左括号（不可能为')'），那么也是直接压入运算符堆栈中；
    c、如果此时遍历到的元素的优先级比此时运算符堆栈栈顶元素的优先级高，则直接压入运算符堆栈；
    d、如果正在遍历的元素的优先级和运算符堆栈栈顶的元素的优先级相等或者更小，则需要将栈顶元素弹出并且放到操作数堆栈中，并且将正在遍历的元素压入到运算符堆栈，其实运算符堆栈中的元素顺序就是优先级的顺序；
5、直到遍历完表达式，此时还需要将运算符堆栈中的所有元素压入到操作数堆栈中，算法完成。
"""


def postfix(list_expr, s_num, s_ope):
    lefty = '([{'
    righty = ')]}'
    for e in list_expr:
        if e.isnumeric():
            s_num.push(e)
        else:
            if e in lefty:
                s_ope.push(e)
            elif e in righty:
                s_ope.push(e)
                sign = s_ope.pop()
                while sign != '(':
                    if sign not in lefty and sign not in righty:
                        s_num.push(sign)
                    sign = s_ope.pop()
            else:
                if s_ope.is_empty():
                    s_ope.push(e)
                elif s_ope.top() == '(':
                    s_ope.push(e)
                elif e < s_ope.top():
                    s_ope.push(e)
                else:
                    s_num.push(s_ope.pop())
                    s_ope.push(e)

    while not s_ope.is_empty():
        s_num.push(s_ope.pop())

    list_after = [None] * s_num.__len__()
    for i in range(s_num.__len__() - 1, -1, -1):
        list_after[i] = s_num.pop()

    return ''.join(list_after)


# 将表达式字符串转化为表达式的列表
def express_list(str):
    l = []
    i = 0
    while i < len(str):
        if not str[i].isnumeric():
            l.append(str[i])
            i += 1
        else:
            j = i + 1
            s = str[i]
            while j < len(str) and str[j].isnumeric():
                s = s + str[j]
                j += 1
            l.append(s)
            i = j
    return l


if __name__ == '__main__':
    str = '((5+2)*(8-3)/4)-5'
    list_expr = express_list(str)
    print(list_expr)
    s_num = ArrayStack()
    s_ope = ArrayStack()
    print(postfix(list_expr, s_num, s_ope))
    while not s_num.is_empty():
        print(s_num.pop(), end='')
