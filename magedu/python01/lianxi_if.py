# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 多分支
a = int(input('>>>>'))

if a < 0:
    print('negative')
elif a == 0:
    print('zero')
else:
    print('postive')

# 多分支嵌套
source = int(input('>>>>'))

if source < 0:
    print('wrong')
else:
    if source == 0:
        print('egg')
    elif source <= 100:
        print('right')
    else:
        print('too big')

## 练习
### 给定一个不超过5位的正整数，判断其有几位
### 使用input函数

num = int(input('>>>'))
if num >= 1000:
    if num >= 10000:
        print(5)
    else:
        print(4)
else:
    if num >= 100:
        print(3)
    elif num >= 10:
        print(2)
    else:
        print(1)

# 给定一个不超过5位的正整数，判断其有几位，依次打印出个位、十位、百位、千位、万位
val = int(input('>>>'))
print(val)

if val >= 1000:
    if val>=10000:
        num = 5
    else:
        num = 4
else:
    if val>=100:
        num = 3
    elif val >= 10:
        num = 2
    else:
        num = 1

print(num)
pre = 0

for i in range(num,0,-1):
    cur = val//(10**(i-1))
    print(cur - pre*10)
    pre = cur