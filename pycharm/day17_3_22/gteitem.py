# -*- coding:utf-8 -*-
class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "192.168.1.1"
                  }

    def __getitem__(self, key):
        return "hello"


data = DataTest(1, "192.168.2.11")
print(data[0])
