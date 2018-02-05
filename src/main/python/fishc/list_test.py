# 列表元素可以为不同数据类型
test_list = ['a_lala', 'b_lala', 'c_lala']
test_list.append('d_lala')
test_list.extend(['e_lala', 'f_lala'])
test_list.insert(0, 'g_lala')
for item in test_list:
    print(item, end=" ")
print()
print('First element in list', test_list[0])

temp = test_list[0]
test_list[0] = test_list[1]
test_list[1] = temp
print(test_list)

# 参数名必须存在
test_list.remove('b_lala')
print(test_list)
# 参数index必须存在
del test_list[0]
print(test_list)
# 参数可选必须存在
print(test_list.pop(0))
print(test_list)

# 分片
print(test_list[1:3])
print(test_list[:])
print(test_list[::2])

# 不同指向的拷贝
test_list2 = test_list[:]
test_list2.append('test')
print(test_list2)
print(test_list)