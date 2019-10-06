# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# else 子句
# 如果循环正常结束，就执行else子句，如果使用break终止，else子句不会执行
# 例子
for i in range(5):
    print(i)
else:
    print('ok')

for i in range(100):
    if i > 50:
        continue
else:
    print('ok')