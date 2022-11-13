# 封裝、繼承與多型

class Animal:

    def __init__(self, name):
        self.name = name

    def structure(self):
        print("heart","leg","body","hand")

    def func(self):
        print("consume", "breath")


class Tiger(Animal):
    def __init__(self, name, color): # 把 parent 的建構子（__init__）呼叫進去
        super().__init__(name) # 刪掉這行看看
        self.color = color

    def structure(self): # if parent have the same function 
        print("My name is " + self.name, "I have heart, leg, body, hand")

    def roar(self):
        print("AAAAAAAAAAAA")


white_tiger = Tiger("lilwhite","white")

white_tiger.structure() # parent 和 child 都有這個function -> method overriding
white_tiger.roar() # parent 沒有，只有child 有
white_tiger.func() # parent 有，child 沒有

print(white_tiger.name)
print(white_tiger.color)
print(issubclass(Tiger,Animal))
print(issubclass(Animal,Tiger))