# 字典举例
dict1 = {
    'a': 'aaa',
    'b': 'bbb',
    'c': 222
}
print(dict1)
print('key: b, value:', dict1['b'])
print('key: c, value:', dict1['c'])

# ---------------------------------------------------------------------------------------------------------

# 或使用{}, dict()
dict2 = {}
dict3 = dict((('F', 70), ('i', 105)))
print(dict3)

# ---------------------------------------------------------------------------------------------------------

# 或使用关键字参数
dist4 = dict(b='b_hahaha', a='a_hahaha')
print(dist4)

# ---------------------------------------------------------------------------------------------------------

# 改变原本没有的key的value，会添加对应的key和value
dist4['d'] = 'd_hahaha'
dist4.setdefault('e', 'e_hahaha')
print(dist4)

# ---------------------------------------------------------------------------------------------------------

# 创建新的字典
dist5 = {}
print(dist5.fromkeys((1, 2, 3), 'Number1'))

# ---------------------------------------------------------------------------------------------------------

# 访问字典的几种方法：keys(), values(), items()
dist6 = {}
dist6 = dist6.fromkeys(range(25), 'test')
for eachKey in dist6.keys():
    print(eachKey, end="; ")
print()
for eachValue in dist6.values():
    print(eachValue, end="; ")
print()
for eachKey, eachValue in dist6.items():
    print(eachKey, ":", eachValue, end="; ")
print()

# ---------------------------------------------------------------------------------------------------------

# get() 方法，安全访问dist
print('value at 55:', dist6.get(55, 'Not found'))
print('value at 24:', dist6.get(24))
# in：查找键是否存在，not in：查找键是否不存在
temp = dist6.get(55) if 55 in dist6 else 'Not found'
print(temp)

# ---------------------------------------------------------------------------------------------------------

# clear() 方法，代替~~={}，推荐使用，因为clear清除的不是赋予新的索引指向，而是清除索引指向的数据值
# 举例，如果a, b同时指向一个字典，用{}方法清除a的数据是没有办法清除b的数据的
# 但使用clear可以清除内存存放的字典的数据，a, b都被清空
dist7 = {}
dist7 = dist7.fromkeys(range(25), 'test')
dist7.clear()

# ---------------------------------------------------------------------------------------------------------

# copy() 方法：浅拷贝：数据相同，而数据地址不同
dist8 = {
    'a': 'aaaaaa',
    'b': 'bbbbbb'
}
a = dist8
b = dist8.copy()
print('normal assign: dist8 id:', id(dist8), '; a id:', id(a))
print('shadow copy: dist8 id:', id(dist8), 'b id:', id(b))

# ---------------------------------------------------------------------------------------------------------

# pop()：指定弹出；popitem()：随机弹出（字典无序）
# update()方法：用已有字典更新其他字典
a = {
    1: 'a',
    2: 'b'
}

b = {
    2: 'c',
    3: 'd'
}
a.update(b)
print('Value of a is:', a)