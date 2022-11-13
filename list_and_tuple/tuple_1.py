# 執行速度比list快，儲存在Tuple的資料比較安全
# 因為不能修改
# list 用的是[]
# tuple用的是()
l = [1,2,3,4]
t = tuple(l)
print(t)

print(t[-1])
t[-1] = 100
l[-1] = 100
print(t)
print(l)