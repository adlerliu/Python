# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 打印一个边长为n的正方形
row = 6
for i in range(row):
    print(' *' * (row), end='')
    print()

row = 6
for i in range(row):
    if (i == 0) or (i == row-1):
        print(' *'*(row), end='')
    else:
        print(' *'+'  '*(row-2)+' *', end='')
    print()

# 求100以内奇数和
# for循环实现

sum = 0
for i in range(1, 100, 2):
    sum += i
print(sum)

sum = 0
for i in range(0, 100):
    if i % 2 != 0:
        print(i, end=' ')
        sum += i
print('\n奇数和是：', sum)

# while循环实现
sum = 0
n = 99
while n > 0:
    sum = n + sum
    n = n - 2
print(sum)

sum = 0
n = 100
while n > 0:
    n = n-1
    if n % 2 != 0:
        print(n, end=' ')
        sum += n
print('\n奇数和：', sum)

# 求100以内偶数和
# for循环实现
sum = 0
for i in range(0, 101, 2):
    sum += i
print(sum)

sum = 0
for i in range(0, 101):
    if i %2 == 0:
        print(i, end='')
        sum += i
print('\n偶数和是：', sum)

# while循环实现
sum = 0
n = 100
while n > 0:
    sum = n + sum
    n = n - 2
print(sum)

sum = 0
n = 101
while n > 0:
    n = n - 1
    if n % 2 == 0:
        print(n, end=' ')
        sum += n
print('\n奇数和：', sum)

# 判断学生成绩，成绩等级A-E。其中，90分以上为'A'，80~89为'B'，70~79为'C'，60~69为'D'，60以下为'E'

num = int(input('>>>'))
if num >= 90:
    if 80 >num >= 89:
        print('B')
    else:
        print('A')
else:
    if 70 > num >= 79:
        print('C')
    elif 60>num >=69:
        print('D')
    else:
        print('E')

# 求1到5的阶乘之和
sum = 0
factorial = 1
num = int(input('请输入一个数字：'))
for i in range(1, num+1):
    factorial = factorial * i
    print(factorial)
    sum += factorial
print('阶乘之和：', sum)

# 给一个数，判断它是否是素数(质数) 质数:一个大于1的自然数只能被1和它本身整除
num = int(input('请输入一个数字：'))
if num <= 1:
    print('这不是质数')
elif num == 2:
    print('这是一个质数')
else:
    i = 2
    while i < num:
        if num % i == 0:
            print('这不是一个质数')
            break
        i += 1
    else:
        print('这是一个质数')

num = int(input('请输入一个数字:'))
if num <= 1:
    print('这不是质数')
elif num == 2:
    print('这是一个质数!')
else:
    for i in range(2,num):
        if num%i == 0:
            print('这不是一个质数')
            break
    else:
        print ('这是一个质数!')




