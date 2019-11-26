# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 求100以内的素数
# 一个数能被从2开始到自己的平方根的正整数整除，就是合数

import math

n = 100
for x in range(2, n):
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            break
    else:
        print(x)

# 求100以内的素数
# 合数一定可以分解为几个质数的乘积

import math

n = 100
primenumber = []
for x in range(2, n):
    for i in primenumber:
        if x % i == 0:
            break
    else:
        primenumber.append(x)
        print(x)

# 求100内的素数

import math

primenumber = []
flag = False
for x in range(2, 100):
    for i in primenumber:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        primenumber.append(x)
        print(x)

# 计算杨辉三角前6行

# 方法一
triangle = [[1], [1,1]]
for i in range(2, 6):
    cur = [1]
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)

# 方法一变体
triangle = []
n = 6
for i in range(n):
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(i-1):
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)
print(triangle)

# 方法二(while方法)
n = 6
oldline = []
newline = [1]
length = 0
print(newline)
for i in range(1, n):
    oldline = newline.copy()
    oldline.append(0)  # 尾部追加0，相当于2端加0
    newline.clear()
    offset = 0
    while offset <= i:
        newline.append(oldline[offset-1]+oldline[offset])
        offset += 1
    print(newline)

# 方法二(for方法)
n = 6
oldline = []
newline = [1]
length = 0
print(newline)
for i in range(1, n):
    oldline = newline.copy()
    oldline.append(0)  # 尾部加0
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1]+oldline[j])
    print(newline)

# 方法三
triange =[]
n = 6

for i in range(n):
    row = [1]  # 开始的1
    for k in range(i): # 中间填0，尾部填1
        row.append(1) if k == i-1 else row.append(0)
    triange.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1): # n=3进来
        val = triange[i-1][j-1] + triange[i-1][j]
        row[j] = val
        if j != i-j:
            row[-j-1] = val
print(triange)

# 方法三变形
triange =[]
n = 6

for i in range(n):
    row = [1]*(i+1)
    triange.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1): # n=3进来
        val = triange[i-1][j-1] + triange[i-1][j]
        row[j] = val
        if j != 2j:
            row[-j-1] = val
print(triange)
