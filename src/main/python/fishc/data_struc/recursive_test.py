# 汉诺塔解决方案

def hanno(num):
    'num defines number of box to be moved'
    def iterateFunc(number, position, destination, usage):
        if number > 0:
            number -= 1
            iterateFunc(number, position, usage, destination)
            print('Move {} --> {}'.format(position, destination))
            iterateFunc(number, usage, destination, position)
    if num > 0:
        iterateFunc(num, 'X', 'Y', 'Z')
    else:
        print('Invalid input')

hanno(5)

# -----------------------------------------------------------------------------------------

def factorial(i):
    if i == 0:
        return 1
    elif i > 0:
        return i * factorial(i - 1)
    else:
        print('Invalid input')
print('5! is', factorial(5))


# -----------------------------------------------------------------------------------------

# 不推荐，耗资源
def fibonacci(i):
    if i <= 2:
        return 1
    elif i > 2:
        return fibonacci(i - 1) + fibonacci(i - 2)

print(list(map(lambda x: fibonacci(x), range(1,21))))