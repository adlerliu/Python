# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 切片
l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])

# 对对象进行切片
s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

# 纯文本形式的收据以一行字符串的形式被解析
invoice = """
... 0.....6..................................40..........52....55............
1909   Pimoroni  PiBrella       $17.50      3       $52.50
1489   6mm Tactile Switch x20   $4.95       2       $9.90
1510   Panavise  Jr. -PV-201    $28.00      1       $28.00
1601   PiTFT Mini  Kit 320x240  $34.95      1       $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# 给切片赋值
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11,22]
print(l)
l[2:5] = [100]
print(l)

# 对序列化使用+和*
l = [1, 2, 3]
print(l * 3)
print(5 * 'abcd')
