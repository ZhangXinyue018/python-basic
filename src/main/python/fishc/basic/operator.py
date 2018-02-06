a = 0
a += 1

# python3: /:返回float; //:返回int
print(3/2)
print(3//2)

# 负数的module是正数
print(5 % 3)
print(-5 % 3)

# **为幂运算:比左侧优先级高，比右侧优先级低
print(3 ** 2)
print(-3 ** 2)
print(3 ** 2 * 2)

print(1 < 2 and 3 < 2)
print(1 < 2 or 3 < 2)
print(not 3 < 2)
print(3 < 4 < 5)

x, y = 4, 5
small = x if x < y else y
print(small)

# assert throws AssertionError if condition is false
assert 4 > 3
# assert 3 > 4