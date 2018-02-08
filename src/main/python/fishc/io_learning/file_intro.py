file = open(r'/Users/zhangxinyue/Documents/pycharm/project_content/python-basic/resource/test.txt')
print(file)

print('Current read pointer at:', file.tell())
# 参数为字符个数，英文char占一个字符，中文char占两个字符
print('First read result:', file.read(2))
print('Current read pointer at:', file.tell())
print('Second read result:', file.read())
print('Third read result:', file.read())
# 不明白
file.seek(0, 0)
print('Fourth read result:', file.read())

# ---------------------------------------------------------------------------------------------------------

print('---------------------------------------------------------------------------')
file.seek(0, 0)
for each_line in file:
    print(each_line)

print('---------------------------------------------------------------------------')
file.close()

# ---------------------------------------------------------------------------------------------------------

file = open(r'/Users/zhangxinyue/Documents/pycharm/project_content/python-basic/resource/test.txt', mode='a')
file.write('\nlalala')
file.close()

