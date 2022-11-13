# 封裝
# 呼叫class內的其他method

class ZZZ:
    def __init__(self,name,situation):
        self.name = name
        self.situation = situation

    def __sleep(self):
        if self.situation == True:
            self.situation = False

    def wake_up(self):
        ZZZ.__sleep(self)
        return self.situation



        


z = ZZZ("Nuss",True)
# z.__sleep()
flag = z.wake_up()

if flag:
    print(f"{z.name} is sleep now")
else:
    print(f"{z.name} is awake now")