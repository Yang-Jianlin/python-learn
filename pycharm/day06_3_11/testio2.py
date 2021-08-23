def process(string):
    print("process:", string)


with open('test_io.txt') as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)
