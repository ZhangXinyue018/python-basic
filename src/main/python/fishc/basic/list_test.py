# 列表元素可以为不同数据类型，列表实质为栈
test_list = ['a_lala', 'b_lala', 'c_lala']
test_list.append('d_lala')
test_list.extend(['e_lala', 'f_lala'])
test_list.insert(0, 'g_lala')
for item in test_list:
    print(item, end=" ")
print()
print('First element in list', test_list[0])

print('-------start test index------')
temp = test_list[0]
test_list[0] = test_list[1]
test_list[1] = temp
print(test_list)
print('-------end test index------')

print('-------start test index delete------')
# 参数名必须存在
test_list.remove('b_lala')
print(test_list)
# 参数index必须存在
del test_list[0]
print(test_list)
print('-------end test index delete------')

# 参数可选必须存在
print(test_list.pop(0))
print(test_list)

# 分片
print(test_list[1:3])
print(test_list[:])
print(test_list[::2])

# 不同指向的拷贝
test_list2 = test_list[:]
test_list3 = test_list.copy()
test_list2.append('test2')
test_list3.append('test3')
print('slide copy', test_list2)
print('method copy', test_list3)
print('original', test_list)

# 列表可拼接，不推荐，推荐使用append，insert和extend
test_list += ['g_lala', 'h_lala']
print(test_list)

print(test_list * 2)

print('123' in test_list)
print('g_lala' in test_list)
test_list *= 2
print(test_list.count('g_lala'))

# 返回第一次出现的index
print(test_list.index('g_lala'))

test_list.reverse()
print(test_list)

test_list.sort(reverse=True)
# test_list.sort()
print(test_list)

# list方法可传参数
a = 'test string'
a = list(a)
print(a)

b = sorted(a)
print(b)
print(a)

b = list(reversed(a))
print(b)
print(a)

b = list(enumerate(a))
print(b)
print(a)

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7]
c = list(zip(a, b))
print(c)