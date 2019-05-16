# -*- encoding=utf-8 -*-
# 切片
# l = [10, 20, 30, 40, 50, 60]
# print(l[:2])
# print(l[2:])
# print(l[:3])
# print(l[3:])

# 对对象进行切片
# s = 'bicycle'
# print(s[::3])
# print(s[::-1])
# print(s[::-2])

# 纯文本文件形式的收据以一行字符串的形式被解析
# invoice = """
# ...0.....6...............................40.........52.....55...........
# 1909 Pimoroni PiBerella
# 1489 6mm Tactile Switch x20
# 1510 Panavise Jr. - PV-201
# 1601 OiTFT Mini Kit 320x240
# """
# SKU = slice(0, 6)
# DESCRIPION = slice(6, 40)
# UNIT_PRICE = slice(40, 52)
# QUANTITY = slice(52, 55)
# ITEM_TOAL = slice(55, None)
# line_items = invoice.split('\n')[2:]
# for item in line_items:
#     print(item[UNIT_PRICE], item[DESCRIPION])

# 给切片赋值
l = list(range(10))
print(l)
print(l[2:5])
l[2:5] = [20, 30]   ## 用[20,30]将取代索引[2，5)的值
print(l)
del l[5:7]
print(l)
l[3:2] = [11, 22]
print(l)
print(l[2])
print(l[5])