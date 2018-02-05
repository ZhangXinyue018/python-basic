# 元组：不可变的列表（不可改，不可加，不可删除）
test_tuple = ('a_haha', 'b_haha', 'c_haha', 7)
for item in test_tuple:
    print(item, end=" ")
print()
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1:3])

# 元组识别：逗号,
temp = (1)
print(type(temp))
temp = 1, 2, 3
print(type(temp))
temp = ()
print(type(temp))
temp = (1, )
print(type(temp))

# 通过创建元组的拷贝的方法，添加元组元素
temp = ('a_lala', 'b_lala', 'c_lala', 'e_lala')
temp = temp[:3] + ('d_lala',) + temp[3:]
print(temp)
