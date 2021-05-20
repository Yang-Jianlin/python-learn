from sixth_chapter.stack import ArrayStack


def comp(num1, num2, e):
    if e == '+':
        return num1 + num2
    if e == '-':
        return num1 - num2
    if e == '*':
        return num1 * num2
    if e == '/':
        return num1 / num2


# 后缀表达式已经将计算的优先顺序排好，
# 只需要将后缀表达式的数字逐个入栈，直到遇到符号，
# 将前栈顶两个元素运算放回栈顶即可
def comp_postfix(expr):
    stack = ArrayStack()
    for e in expr:
        if e.isnumeric():
            stack.push(e)
        else:
            num = comp(num2=int(stack.pop()), num1=int(stack.pop()), e=e)
            stack.push(num)

    return stack.pop()


if __name__ == '__main__':
    expr = '52+83-*4/5-'
    print(comp_postfix(expr))
