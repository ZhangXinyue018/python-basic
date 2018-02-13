import random as r
# 变量或函数前面加两个下划线__，则声明为私有(name mangling)，会变成：_类名__变量名（伪私有）
class Ball:
    __test = 'alalala'
    def __init__(self, name):
        self.name = name
    def getTest(self):
        return self.__test
    def kick(self):
        print('Kicked', self.name)

ball = Ball('new ball A')
ball.kick()
# print(ball.__test) raise AttributeError
print(ball.getTest())


print('------------------------------------inheretance test----------------------------------------------------')

# python支持多重继承
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        self.x -= 1
        print('fish position:', self.x, self.y)

class Selmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True
    def eat(self):
        print('shark eat') if self.hungry else print('not hungry')
        self.hungry = False

class Cutie:
    def printSelf(self):
        print('I\'m cutie')


class Dory(Fish, Cutie):
    pass
print('------------------------------------selmon test----------------------------------------------------')
selmon = Selmon()
selmon.move()
print('------------------------------------shark test----------------------------------------------------')
shark = Shark()
shark.eat()
shark.eat()
shark.move()
shark.move()
print('------------------------------------dory test----------------------------------------------------')
dory = Dory()
dory.move()
dory.printSelf()