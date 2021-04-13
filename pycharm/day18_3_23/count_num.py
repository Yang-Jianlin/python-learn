class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


print(Student.count)
s = Student('Bart')
print(s.count)
s = Student('Bart')
print(s.count)
