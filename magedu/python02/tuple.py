# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 依次接收用户输入的3个数，排序后打印
# 1、使用int后，判断大小排序
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))

if nums[0] > nums[1]:
    if nums[0] > nums[2]:
        i3 = nums[0]
        if nums[1] > nums[2]:
            i2 = nums[1]
            i1 = nums[2]
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i2 = nums[0]
        i3 = nums[2]
        i1 = nums[1]
else:
    if nums[0] > nums[2]:
        i3 = nums[1]
        i2 = nums[0]
        i1 = nums[2]
    else:
        if nums[1] < nums[2]:
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
        else:
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
print(i1,i2,i3)

# 改进如下
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}:'.format(i))))
if nums[0] > nums[1]:
    if nums[1] > nums[2]:
        if nums[1] > nums[2]:
            out = [2, 1, 0]
        else:
            out = [1, 2, 0]
    else:
        out = [1, 0, 2]
else:
    if nums[0] > nums[2]:
        out = [2, 0, 1]
    else:
        if nums[1] < nums[2]:
            out = [0, 1, 2]
        else:
            out = [0, 2, 1]
out.reverse()
for i in out:
    print(nums[i], end=',')

# 2、使用max函数实现
num = []
out = None
for i in range(3):
    num.append(int(input('{}: '.format(i))))

while True:
    cur = min(num)
    print(cur)
    num.remove(cur)
    if len(num)  == 1:
        print(num[0])
        break

# 3、列表sort实现
nums = []
out = None
for  i in range(3):
    nums.append(int(input('{}: '.format(i))))
nums.sort()
print(nums)

# 4、冒泡实现
num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
length = len(nums)
for i in range(length):
    for j in range(length-i-1):
        if nums[j] > nums[j-1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)

# 冒泡法优化
num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
length = len(nums)
for i in range(length):
    flag =False
    for j in range(length-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            flag =True
    if not  flag:
        break
print(nums)

































