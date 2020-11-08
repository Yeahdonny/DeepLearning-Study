# -*- coding: utf-8 -*-
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
        
    def hello(self):
        print("HELLO "+self.name + " !")
        
    def goodbye(self):
        print("Goodbye " + self.name + " !")

m = Man("David")
m.hello()
m.goodbye()
