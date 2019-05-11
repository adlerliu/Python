# -*- encoding=utf-8 -*-

# 输出两个数，比较大小后，从小到大升序打印
# a = int(input('>>>'))
# b = int(input('>>>'))
#
# if a >= b:
#     print(b, a)
# else:
#     print(a, b)

# 三目运算符
# a = int(input('first: '))
# b = int(input('second: '))
# print(b, a) if a>=b else print(a, b)

# 给一个半径，求圆的面积和周长。圆周率3.14
# r = int(input('>>>'))
# π = 3.14
# s = (π*r*r)
# b = (2*π*r)
# print('圆的面积', s)
# print('圆的周长', b)

# 输入n个数，求每次输入后算平均数

# count = 0
# sum = 0
# while True:
#     num = int(input('>>>'))
#     count += 1
#     sum += num
#     print(count/sum)

# n = int(input('输入n个数:'))
# count = 0
# sum = 0
# for i in range(0,n):
#     x = int(input('>>>'))
#     sum += x
#     count += 1
#     print(sum/count)

# n = 0
# sum = 0
# while True:
#     i = input('>>')
#     if i == 'None':
#         break
#     n += 1
#     sum += int(i)
#     avg = sum/n
#     print(avg)

# 九九乘法表
# for i in range(10):
#     b = 1
#     while b <= i:
#         print('{}*{} {}{:<4}'.format(b, i, '=', b*i),end='')
#         b += 1
#     print()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(str(j)+'*'+str(i)+"="+str(i*j),end=' ')
#     print()

# for i in range(1,10):
#     for j in range(1,1+i):
#         product = i*j
#         if j>1 and product<10:
#             product = str(product)+' '
#         else:
#             product = str(product)
#         print(str(j)+'*'+str(i)+'='+product,end=' ')
#     print()

# for i in range(1,10):
#     line = ''
#     for j in range(1,i+1):
#         line += '{0}*{1}={1:<2}'.format(j,i,i*j)
#     print(line)

# for i in range(1,10):
#     line = ''
#     for j in range(1,i+1):
#         line += '{}*{}={:<3}'.format(j,i,i*j)
#     print(line)

# 打印九九乘法表方阵的上半部分
# for i in range(1,10):
#     print(' '*7*(i-1),end='')
#     for j in range(i,10):
#         product = i*j
#         if product < 10:
#             end = ' '
#         else:
#             end = ' '
#         print(str(i)+'*'+str(j)+'='+str(i*j), end=end)
#     print()

# for i in range(1,10):
#     for j in range(i):
#         print('      ',end=' ')
#     for m in range(i,10):
#         print('{0}*{1}={2:<2}'.format(i,m,i*m),end=' ')
#     print()

# 打印菱形

# s = '*'
# for i in range(1, 8, 2):
#     print((s*i).center(7))
# for i in reversed(range(1, 6, 2)):
#     print((s*i).center(7))

# for i in range(-3,4):
#     if i<0:
#         prespace = -i
#     else:
#         prespace = i
#     print(' '*prespace+'*'*(7-prespace*2))

# #  空心菱形

# rows = int(input('输入列数： '))
# i = j = k = 1
# #  声明变量,i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# #  打印菱形
# print("打印空心等菱形，这里去掉if-else条件判断就是实心的")
# for i in range(rows):
#     for j in range(rows - i):
#         print(" ", end=" ")
#         j += 1
#     for k in range(2 * i - 1):
#         if k == 0 or k == 2 * i - 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         k += 1
#     print ("\n")
#     i += 1
#     #  菱形的下半部分
# for i in range(rows):
#     for j in range(i):
#         #  (1,rows-i)
#         print(" ", end=" ")
#         j += 1
#     for k in range(2 * (rows - i) - 1):
#         if k == 0 or k == 2 * (rows - i) - 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         k += 1
#     print("\n")
#     i += 1

# 打印闪电
# for i in range(-3,4):
#     if i<0:
#         print(' '*(-i)+'*'*(4+i))
#     elif i>0:
#         print(' '*3+'*'*(4-i))
#     else:
#         print('*'*7)

# j = '*'
# for i in range(-3,4):
#     if i == 0:
#         print(j*7)
#     print(' '*(-i)+j*(i+4)) if i<0 else print(3*' '+j*(3-i))

# 斐波那契数列，100以内
# print(0)
# print(1)
# a = 0
# b = 1
# while True:
#     c = a + b
#     if c > 100:
#         break
#     a = b
#     b = c
#     print(c)

# a = 0
# b = 1
# if a == 0:
#     print(1)
# for i in range(100):
#     c = a + b
#     a = b
#     b = c
#     if c < 100:
#         print(c)

# 封装，结构方法
# i, j = 0, 1
# while i < 100:
#     print(i)
#     i, j = j, i+j

# 斐波那契数列第101项
# a = 1
# b = 1
# index = 2
# print('{0},{1}'.format(0,0))
# print('{0},{1}'.format(1, 1))
# print('{0},{1}'.format(2,1))
# while True:
#     c = a + b
#     a = b
#     b = c
#     index += 1
#     print('{0},{1}'.format(index, c))
#     if index == 101:
#         break

# i = 1
# j = 1
# count = 1
# while True:
#     i, j = j, i+j
#     count += 1
#     if count == 101:
#         break
# print(count, i)

# i = 1
# j = 1
# count = 1
# for a in range(1, 100):
#     i, j = j, i+j
#     count += 1
#     if count == 101:
#         break
# print(count, j)

# 求10w内所有素数

# import datetime
# start = datetime.datetime.now()
# a = []
# n = 100000
# for i in range(3,n,2):
#     if i > 10 and i % 10 == 5:
#         continue
#     if i > 10 and i % 10 != 1 and i % 10 != 3 and i % 10 != 7 and i % 10 != 9:
#         continue
#     for j in range(3,int(i**0.5)+1,2):
#         if i % j == 0:
#             break
#     else:
#         a.append(i)
# t_time = (datetime.datetime.now()-start).total_seconds()
# print(a)
# print(t_time)

# import datetime
# start = datetime.datetime.now()
#
# for x in range(2,10000):
#     for i in range(2,x):
#         if x % i == 0:
#             break
#     else:
#         print(x)
#
# t_time = (datetime.datetime.now()-start).total_seconds()
# print(t_time)

# import datetime
# start = datetime.datetime.now()
#
# for x in range(2,10000):
#     for i in range(2,int(x **0.5)+1):
#         if x %i == 0:
#             break
#     else:
#         print(x)
# t_time = (datetime.datetime.now()-start).total_seconds()
# print(t_time)

# import datetime
# start = datetime.datetime.now()
#
# for x in range(3,10000,2):
#     for i in range(3,int(x**0.5)+1,2):
#         if x%i ==0:
#             break
#     else:
#         print(x)
# t_time = (datetime.datetime.now()-start).total_seconds()
# print(t_time)

# 完整代码如下

# 方法1：
# import datetime
# upper_limit = 100000
# delta = [0,0]
# counts = [0,0]
#
# start = datetime.datetime.now()
# for _ in range(10):
#     counts[0] = 0
#     for x in range(2,upper_limit):
#         for i in range(2,int(x**0.5)+1):
#             if x % i == 0:
#                 break
#         else:
#             print(x)
#             counts[0] += 1
# delta[0] = (datetime.datetime.now()-start).total_seconds()
# print(delta,sep='\t')
# print(counts,sep='\t')

# import datetime
# upper_limit = 100000
# delta = [0,0]
# counts = [0,0]
#
# start = datetime.datetime.now()
# for _ in range(10):
#     counts[0] = 0
#     for x in range(3,upper_limit,2):
#         for i in range(3,int(x**0.5)+1,2):
#             if x % i == 0:
#                 break
#         else:
#             print(x)
#             counts[0] += 1
# delta[0] = (datetime.datetime.now()-start).total_seconds()
# print(delta,sep='\t')
# print(counts,sep='\t')

# 猴子吃桃问题

peach = 1
for i in range(9):
    peach = 2*(peach+1)
print(peach)


