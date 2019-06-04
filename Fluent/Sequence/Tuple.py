# -*- encoding=utf-8 -*-
"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
warehouse：https://github.com/adlerliu/Python/tree/devops
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 用生成器表达式初始化元组和数组
symbols = 'a_#$%s1'
abc = tuple(ord(symbol) for symbol in symbols)
print(abc)
