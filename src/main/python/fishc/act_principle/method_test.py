def my_first_func():
    print('first function')

def my_second_func():
    print('second function')

def my_third_func(name):
    print('third function with name:', name)

# 形参与实参：num1，num2：形参，传递进来的数值为实参
def my_fourth_func(num1, num2 = 7):
    '''这是一个文档，请在此处填写形参相关信息'''
    print('fourth function to add {} + {} = {}'.format(num1, num2, num1 + num2))
    return num1 + num2

# 收集参数
def my_fifth_func(*params, name):
    '''传说中的收集参数，参数数量不确定，传进来的实参被打包成元组'''
    print('fifth function with param length of', len(params))
    print('second param is', params[1])
    print('name is', name)

my_first_func()
my_second_func()
my_third_func('lalala')
# 关键字参数可以指定参数，优先级高于顺序，推荐使用
num3 = my_fourth_func(num2=2, num1=3)
num3 = my_fourth_func(1)
print(num3)
my_fifth_func(1, 'hahaha', 1231, [1, 2, 3, 4], name='lalala')