# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 打印1~10
for i in range(10):
    print(i+1)

for i in range(1,11):
    i = 11-i
    print(i)

for i in range(10, 0, -1):
    print(i)
# continue语句
# 计算10以内的偶数(for循环)
for i in range(10):
    if not i%2:
        print(i)

for i in range(0,10,2):
    print(i)

for i in range(10):
    if i % 2 ==0:
        continue
    else:
        print(i)

