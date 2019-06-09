# -*- encoding=utf-8 -*-
"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 用生成器表达式初始化元组
symbols = 'a_#$%s1'
abc = tuple(ord(symbol) for symbol in symbols)
print(abc)
# 用生成器表达式初始化数组
import array
abc = array.array('I', (ord(symbol) for symbol in symbols))
print(abc)

# 使用生成器表达式计算笛卡尔积
colors = ['black', 'while']
sizes = ['S', 'M', 'L']
# for循环实现
for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)
# 列表推导式
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
# 生成器表达式
tshirts = tuple((color, size) for color in colors for size in sizes)
print(tshirts)

# 把元组用作记录
lax_coordinates = (33.9425, -118.408056)
# 元组的封装解构
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for循环实现
for passport in sorted(traveler_ids):
    print('%s %s' % passport)
# 利用列表推导式实现
passport = (sorted(s) for s in traveler_ids)
for i in passport:
    print(i)

# 封装解构
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient)
print(remainder)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, a, b ,c = range(5)
print(head, a, b, c)

# 用嵌套元组获得经度
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

# 定义和使用具名元组
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
toyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(toyo)
print(toyo.population)
print(toyo.coordinates)
print(toyo[1])

# 具名函数的属性和方法(上一个的继续)
print(City._fields)
Latlong = namedtuple('Latlong', 'Lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
