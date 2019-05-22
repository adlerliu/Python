# -*- encoding=utf-8 -*-

# 一个简单的二维向量类
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # return 'Vector(%r, %r)' %(self.x, self.y)
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
        return Vector(self.x  *  scalar, self.y * scalar)

## 它能把一个对象用字符串的形式表现出来
test = Vector()
print(test)