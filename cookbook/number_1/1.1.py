# -*- encoding=utf-8 -*-

# 我们有一个包含N个元素的元组或序列，现在想把它分解成N个单独的变量

# p = (4, 5)
# x, y = p
# print(x)
# print(y)

# data = ['ACME', 50, 91.1, [2012, 12, 21]]
# name, shares, price, date = data
# print(name)
# print(shares)
# print(price)
# print(date)

# name, shares, price, (year, mon, day) = data
# print(name)
# print(year)
# print(mon)
# print(day)

# s = 'Hello'
# a, b, c, d, e = s
# print(a, b, c, d, e)

data = ['ACME', 50, 90.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)