# 闭包：即一个函数的返回值为另一个函数（函数式编程），类似于java的lambda interface implementation
def closure_func_a(x):
    def closure_func_b(y):
        return x * y
    return closure_func_b

i = closure_func_a(5)
print(i(4))


# ---------------------------------------------------------------------------------------------------------


# lambda表达式，冒号前面是参数，冒号后面是返回值，结果是匿名的函数
func_lambda_test_1 = lambda x: (2 * x + 1)
print('lambda func 1 result:', func_lambda_test_1(1))

func_lambda_test_2 = lambda x, y: x + y
print('lambda func 2 result:', func_lambda_test_2(2, 5))


# ---------------------------------------------------------------------------------------------------------


# 测试bif之filter
a = list(range(0, 100))
b = list(filter(lambda x: not x % 11, a))
print('a with values:', a)
print('b with values:', b)


# ---------------------------------------------------------------------------------------------------------


# 测试bif之map
print(list(map(lambda x: x * 2, range(10))))