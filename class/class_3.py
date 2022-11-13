# 多型
# 繼承了相同的類別，呼叫相同的函式，但結果卻不同

class Employee:
    def work(self):
        print("Employee work")
 
class worker1(Employee):
    def work(self):
        print("hello work1")
 
class worker2(Employee):
    def work(self):
        print("hello work2")
 
 
w = Employee()
w1 = worker1()
w2 = worker2()
 
w.work()
w1.work()
w2.work()
 