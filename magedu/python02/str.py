# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 字符串练习
# 用户输入一个数字
"""
1、判断是几位数
2、打印每一位数字及其重复的次数
3、依次打印每一位数字，顺序个、十、百、千、万位
"""
num = ''
# 数字输入的简单判断
while True:
    num = input('Input a positive number >>>').strip().lstrip('0')
    if num.isdigit():
        break
print("The length of {} is {}".format(num, len(num)))
#
# 倒序打印1
for i in range(len(num),0,-1):
    print(num[i-1],end=' ')
print()

# 倒序打印2
for i in reversed(num):
    print(i, end=' ')
print()

# 负索引方式打印
for i in range(len(num)):
    print(num[-i-1], end=' ')
print()

# 判断0-9的数字在字符串中出现的次数，每一次迭代都是用count，都是o(n)问题
counter = [0]*10
for i in range(10):
    counter[i] = num.count(str(i))
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))
print('~'*20)

# 迭代字符串本身的字符
counter = [0]*10
for x in num:
    i = int(x)
    if counter[i] == 0:
        counter[i] = num.count(x)
        print("The count of {} is {}".format(x, counter[i]))
print('~'*20)

# 迭代字符串本身的字符
counter = [0]*10
for x in num:
    i = int(x)
    counter[i] += 1

for i in range(len(counter)):
    if counter[i]:
        print("The count of {} is {}".format(i, counter[i]))

# 输入5个数字，打印每个数字的位数，将这些数字排序打印，需求升序打印
nums = []
while len(nums) < 5:
    num = input("Please input a number:").strip().lstrip('0')
    if not num.isdigit():
        continue
    print('The length of {} is {}'.format(num, len(num)))
    nums.append(int(num))
print(nums)

# sort方法排序
lst = nums.copy()
lst.sort()
print(lst)

# 冒泡法
for i in range(len(nums)):
    flag = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            flag = True
    if not flag:
        break
print(nums)