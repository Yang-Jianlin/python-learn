from sixth_chapter.stack import ArrayStack


def reverse_file(filename):
    S = ArrayStack()
    with open(filename, 'r') as original:
        for line in original.readlines():
            S.push(line.rstrip('\n'))
 
    with open(filename, 'w') as output:
        while not S.is_empty():
            output.write(S.pop()+'\n')


if __name__ == '__main__':
    reverse_file('data.txt')
