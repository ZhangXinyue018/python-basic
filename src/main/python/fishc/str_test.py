test_str = 'this is A test String'
for item in test_str:
    print(item, end=" ")
print()
print(test_str[:7])

# 拼接插入字符串
new_str = test_str[:3] + 'test insert' + test_str[3:]
print(new_str)

print(test_str.capitalize())
print(test_str.casefold())

print(test_str.join('******'))
print('*'.join(test_str))
print(test_str.rpartition(' '))
print(test_str.split())
print(test_str.replace(' ', ''))

# format method
# 位置参数方法
print('{0} is a {1} string'.format('this', 'test'))
# 关键字参数方法
print('{a} is a {b} string'.format(a='this', b='test'))
# 花括号打印方法
print('{{lalalalal}}'.format('none'))
# 精确表示法(定点数与浮点数？？？)
print('{0:.3f} test'.format(27.5665))

# 字符串格式化操作符
print('%c %c %c' % (97, 98, 99))
print('%d + %d = %d' % (4, 5, 9))
# #用于给出标识
print('%#o + %#o = %o' % (12, 14, 26))
print('%#X + %#X = %X' % (12, 14, 26))
# 百分号定点数（默认6位）
print('%.3f' % (4/3))
# 自动确定使用%f或%e
print('%G' % (4/3))