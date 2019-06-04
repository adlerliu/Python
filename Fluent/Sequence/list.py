# -*- encoding=utf-8 -*-
"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
warehouse：https://github.com/adlerliu/Python/tree/devops
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 把一个字符变成Unicode码位的列表
# 方法一
symbols = 'a_#$%s1'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# 把一个字符变成Unicode码位的列表
# 方法二
symbols = 'a_#$%s1'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# 用列表推导和map/filter组合起来创建同样的表单
symbols = 'a_#$%s1'
# 列表推导式
beyond_ascil = [ord(s) for s in symbols if ord(s) > 37]
print(beyond_ascil)
# lambda函数创建
beyond_ascil = list(filter(lambda c: c > 37, map(ord, symbols)))
print(beyond_ascil)

# 使用列表推导计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# 列表推导式
tshirts = [(colors, sizes) for color in colors for size in sizes]
print(tshirts)
# for循环实现
for color in colors:
    for size in sizes:
        print(color, size)


