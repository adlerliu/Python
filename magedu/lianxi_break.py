# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# break 语句，终止当前循环
# 计算1000以内的能被7整除的前20个数（for循环)

count = 0
for i in range(0, 1000, 7):
    print(i)
    count += 1
    if count >= 20:
        break

# 计算1000以内的能被7整除的前20个数（while循环)
count = 0
i = 0

while True:
    print(i)
    i += 7
    count += 1
    if count == 20:
        break

