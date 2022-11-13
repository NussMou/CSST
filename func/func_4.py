def long_func(*info):
    print(info[5])
long_func(1,2,3,4,5,6,7,)

def long_func_2(**info):
    print(info["name"])
long_func_2(name='Nuss',school='NTHU')