class Person:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def comSalary(self):
        return float(self.salary)


class Worker(Person):
    def __init__(self, id, name, hours, h_salary):
        super().__init__(id, name, h_salary)
        self.hours = hours

    def comSalary(self):
        return float(self.hours * self.salary)


class SaleMan(Person):
    def __init__(self, id, name, sale_balance, ratio):
        super().__init__(id, name, sale_balance)
        self.ratio = ratio

    def comSalary(self):
        return float(self.salary * self.ratio)


class Manager(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)


class SaleManager(Person):
    def __init__(self, id, name, salary, sale_balance, ratio):
        super().__init__(id, name, salary)
        self.sale_balance = sale_balance
        self.ratio = ratio

    def comSalary(self):
        print(float(self.sale_balance * self.ratio))
        return self.salary + float(self.sale_balance * self.ratio)


if __name__ == '__main__':
    worker = Worker('100010', '王五', 250, 50)
    sale_man = SaleMan('100012', '张三', 180000, 0.20)
    manager = Manager('100001', '赵四', 86500)
    sale_manager = SaleManager('100008', '黄六', 8000, 260000, 0.273)

    w_Salary = worker.comSalary()
    man_Salary = sale_man.comSalary()
    m_Salary = manager.comSalary()
    manager_Salary = sale_manager.comSalary()

    print('姓名：{0}， ID：{1}， 工资：{2}'.format(worker.getName(),
                                          worker.getId(), w_Salary))
    print('姓名：{0}， ID：{1}， 工资：{2}'.format(sale_man.getName(),
                                          sale_man.getId(), man_Salary))
    print('姓名：{0}， ID：{1}， 工资：{2}'.format(manager.getName(),
                                          manager.getId(), m_Salary))
    print('姓名：{0}， ID：{1}， 工资：{2}'.format(sale_manager.getName(),
                                          sale_manager.getId(), manager_Salary))
