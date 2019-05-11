# -*- encoding=utf8 -*-

# 一个简单的二维向量类
from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # def __repr__(self):
    #     #     return 'Vector(%r, %r)' %(self.x, self.y)
    def __repr__(self):
        return '{}{:>2}{:>2}'.format('Vector', self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __matmul__(self, scalar):
        return Vector(self.x * scalar,self.y*scalar)
# 它能把一个对象用字符串的形式表现出来
test = Vector()
print(test)
# test #如果注释 __repr__() 方法, 显示 <__main__.Vector at 0x7f587c4c1320>

# __repr__() 能把一个对象用字符串的方式表达出来，这就是字符串表示形式。它的返回应该尽量精确的与表达出创建它的对象,
# 与 __str__() 比较， __str__() 是由 str() 函数调用，并可以让 print() 函数使用。并且它返回的字符串应该对终端用户更友好。
# 如果你只想实现这两个方法的其中一个，好的选择是 __repr__()，因为一个对象没有 __str__() 函数，python 又要调用它的时候，
# 解释器会使用 __repr__() 来代替。
print(str(test))
# + 和 * 分别调用的是 __add__ 和 __mul__ 注意这里我们没有修改 self.x, self.y，
# 而是返回了一个新的实例，这是中缀表达式的基本原则，不改变操作对象
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1+v2)


def __bool__(self):
    return bool(abs(self))
# 优化写法
# 如果想要 Vector.__bool__ 更高效，可以采用这种实现

#def __bool__(self):
#    return bool(self.x or self.y)
# 把返回值显式转成 bool 格式是为了符合 __bool__() 对返回值的规定，
# 因为 or 运算符可能返回 x 或 y 本身的值，如果 x 为真，
# 返回的是 x 值，y 为真，返回的是 y 的值