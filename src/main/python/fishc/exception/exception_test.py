# 方法把异常抛上去
def test_error(a):
    if a == 0:
        raise ZeroDivisionError('test error')

print()
print('-------------------------------test try--------------------------------------------------')
try:
    a = int(input('Enter first: '))
    b = int(input('Enter second: '))
    print(a/b)
except (OSError, ValueError) as reason:
    print('OS or Value Error:', str(reason))
except ZeroDivisionError:
    print('Zero Division Error:')
finally:
    print('End')

print('-------------------------------test else--------------------------------------------------')
# else语句应用场景：1. 与if搭配；2. 与循环搭配，for，while，如果循环由break跳出，则else不执行；3. 与异常处理搭配
try:
    a = int(input('Enter test value: '))
    test_error(a)
except ZeroDivisionError as reason:
    print('Error: ', str(reason))
# else不会捕获任何异常，会对没有捕获任何异常的情况进行处理
else:
    print('No error')

print('---------------------------------test with------------------------------------------------')
# with语句
try:
    with open('file_not_exist.try', mode='r') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('OS Error:', str(reason))
print('---------------------------------------------------------------------------------')