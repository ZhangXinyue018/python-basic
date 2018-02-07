# 不管初始化参数怎样，集合中元素唯一，集合无序
num = {1, 2, 3, 4, 5, 5}
print('Type of num is:', type(num))
print('Value of num is:', num)

# 使用set()初始化
num1 = set([1, 2, 4, 4])
print('Value of num1 is:', num1)
num1.add(6)
print('Value of num1 is:', num1)
num1.remove(2)
print('Value of num1 is:', num1)

# ---------------------------------------------------------------------------------------------------------

# 不可变集合
num2 = frozenset([1, 1, 2, 3, 4, 5])
print('Value of num2 is:', num2)