# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 冒泡法定义
"""
属于交换排序
两两比较大小，交换位置。
结果分为升序和降序排列
"""
# 升序
"""
n个数从左至右，编号从0开始到n-1，索引0和1的值比较，如果索引0大，则交换两者位置，如歌索引1大，则不交换。
继续比较索引1和2的值，将大值放到右侧。直至n-2和n-1比较完，第一轮比较完成。
第二轮从索引0比较到n-1，因此最右侧n-1位置上已经是最大值。以此类推，每一轮都会减少最右侧不参与比较，直至剩下最后2个数比较。
"""
# 降序
# 和升序相反

# 冒泡代码实现一
num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9]]
nums = num_list[0]
print(nums)
length = len(nums)
count_swap = 0
count = 0

for i in range(length):
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            count_swap += 1
print(nums)

num_list = [[1,9,8,5,6,7,4,3,2],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,9,8]]
nums = num_list[0]
print(nums)
length = len(nums)
count_swap = 0
count = 0
for i in range(length):
    flag = False
    for j in range(length-i-1):
        count += 1
        if nums[j] > nums[j+1]:  #降序反之
            nums[j],nums[j+1] = nums[j+1],nums[j]
            flag = True
            count_swap += 1
    if not flag:
        break
print(nums)