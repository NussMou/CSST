# 多重繼承
# 一個 subclass 繼承了多個 class

class Drinkable:
    def say():
        print("yummy")

class Soup:
    def say():
        print("hot and yummy")
        

class Tea(Drinkable, Soup): # 茶是一種蔬菜湯
    pass

# class Tea(Soup,Drinkable): # 茶是一種蔬菜湯
#     pass

Tea.say()
# Tea().say()

