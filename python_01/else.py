# -*- encoding=utf-8 -*-
## break 语句，终止当前循环
# 计算1000以内的能被7整除的前20个数（for循环)
## 两种写法如下所示
# count = 0

# for i in range(0,1000,7):
#     print(i)
#     count += 1
#     if count >= 20:
#         break

# count = 0
# i= 0

# while True:
#     print(i)
#     i += 7
#     count += 1
#     if count == 20:
#         break

## 给定一个不超过5位的正整数，判断其有几位，依次打印出个位、十位、百位、千位、万位
val = int(input('>>>'))
print(val)

if val >= 1000: # ܑԡ
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

# else 子句
# 如果循环正常结束，就执行else子句，如果使用break终止，else子句不会执行
# 例子
for i in range(5):
    print(i)
else:
    print('ok')

for i in range(100):
    if i > 50:
        break
else:
    print('ok')