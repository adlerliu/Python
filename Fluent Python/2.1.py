# -*- encoding=utf-8 -*-
# 使用列表推导式计算笛卡尔积
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirs = [(color, size) for color in colors for size in sizes]
# print(tshirs)
#
# for color in colors:
#     for size in sizes:
#         print((color, size))
#
# tshirs = [(color, size) for size in sizes for color in colors]
# print(tshirs)

# 用生成器表达式初始化元组和数组
# symbols = 'abcdef'
# a = tuple(ord(symbol) for symbol in symbols)
# print(a)
#
# import array
# a = array.array('I', (ord(symbol) for symbol in symbols))
# print(a)

# 使用生成器表达式计算笛卡尔积
# colors = ['black', 'white']
# sizes = [ 'S', 'M', 'L']
# for tshirt in ('%s %s'%(c, s) for c in colors for s in sizes):
#     print(tshirt)

# 把元组用作记录
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
# print('------------------------------------------')
# for cuntry, _ in traveler_ids:
#     print(cuntry)

# lax_coordinates = (33.9425, -118.408056)
# latitude, longiyude = lax_coordinates
# print(latitude)
# print(longiyude)

# divmod(20, 8)
# t = (20, 8)
# divmod(*t)
# print(t)
# quotient, remainder = divmod(*t)
# print(quotient, remainder)

# import os
# _, filename = os.path.split('/home/liciano/.ssh/idrsa.pub')
# print(filename)
#
# a, b, *rest = range(5)
# print(a, b, rest)
# a, b, *rest = range(3)
# print(a, b, rest)
# a, b, *rest = range(2)
# print(a, b, rest)

# a, *body, c, d = range(5)
# print(a, body, c, d)
# *head, b, c, d = range(5)
# print(head, b, c, d)

# metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
#                ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#                ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#                ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#                ('Sao Paulo', 'BR', 19.694, (-23.547778, -46.635833))]
# print(('{:15} | {:^9} |{:^9}'.format('', 'lat.', 'long.')))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latitude, longitude))

# 定义和使用具名函数
from collections import namedtuple
Ctty = namedtuple('City', 'name country population coordinates')
tokyo = Ctty('Tokyo', 'JP', 36.33, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])

# 具名元组的属性和方法
# print(Ctty._fields)
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = Ctty._make(delhi_data)
# print(delhi)
# print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key +':', value)
