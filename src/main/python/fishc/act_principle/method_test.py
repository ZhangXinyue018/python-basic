# 函数：有返回值；过程：没有返回值
# 严格来说python只有函数没有过程
# 因为所有返回都是None，type为NoneType
def my_first_func():
    print('first function')
my_first_func()


# ---------------------------------------------------------------------------------------------------------


def my_second_func():
    print('second function')
my_second_func()


# ---------------------------------------------------------------------------------------------------------


def my_third_func(name):
    print('third function with name:', name)
my_third_func('lalala')


# ---------------------------------------------------------------------------------------------------------


# 形参与实参：num1，num2：形参，传递进来的数值为实参
def my_fourth_func(num1, num2 = 7):
    '''这是一个文档，请在此处填写形参相关信息'''
    print('fourth function to add {} + {} = {}'.format(num1, num2, num1 + num2))
    return num1 + num2
# 关键字参数可以指定参数，优先级高于顺序，推荐使用
num3 = my_fourth_func(num2=2, num1=3)
num3 = my_fourth_func(1)
print(num3)


# ---------------------------------------------------------------------------------------------------------

# 收集参数
def test_multi_param(*params, name):
    '''传说中的收集参数，参数数量不确定，传进来的实参被打包成元组'''
    print('fifth function with param length of', len(params))
    print('second param is', params[1])
    print('name is', name)
test_multi_param(1, 'hahaha', 1231, [1, 2, 3, 4], name='lalala')


# ---------------------------------------------------------------------------------------------------------

# 如果没有中括号，数据之间只有逗号相连则为元组，因为元组的初始化可以没有小括号
def test__multi_return():
    return [1, 2, 3, 4]
test = test__multi_return()
test.append(5)
print(test)


# ---------------------------------------------------------------------------------------------------------

# 变量的作用域：局部变量，全局变量；如果局部变量名字与全局变量相同，python会用shadow屏蔽的方式，创建新的变量保护全局变量
def test_local_var(num):
    num += 1
    # global 关键字用于定义方法中的变量，使之指向全局变量，用以修改全局变量
    global test_global
    test_global = 5
    return num
num = 1
test_global = 1
print('global var pre:', test_global)
print('return value for num = 1:', test_local_var(num))
print('expect num = 1:', num)
num = 3
print('return value for num = 3:', test_local_var(num))
print('expect num = 3:', num)
print('global var after:', test_global)


# ---------------------------------------------------------------------------------------------------------



# 内嵌函数：作用域在只在其外部函数
def inner_func1():
    print('inner func 1')
    def inner_func2():
        print('inner func 2')
    inner_func2()
inner_func1()


# ---------------------------------------------------------------------------------------------------------




# nonlocal关键字用于使用外部函数的变量值
def Func1():
    x = 5
    def Func2():
        nonlocal x
        x *= x
        print('x in func2 is', x)
        return x
    print('x in func1 is', x)
    return Func2()

print('func 1 result is', Func1())