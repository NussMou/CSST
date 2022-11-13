# basic

class ClassBasic: # notice the class name

    def __init__(self,name,school): # 建構子
        self.name = name # attribute
        self.sch = school

    def say_my_name(self): # method
        print("My name is " + self.name)

    def say_my_school(self):
        print("My school is " + self.sch)

me = ClassBasic("Nuss","NTHU") # declare me is ClassBasic type object

print(type(me))

print(me)

me.say_my_name()
me.say_my_school()


