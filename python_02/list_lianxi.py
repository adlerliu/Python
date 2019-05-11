# -*- encoding=utf-8 -*-

# 求100以内的素数

# Prime = []
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         Prime.append(i)
# print(Prime)

# Prime = []
# for x in range(2,100):
#     for i in range(2,int(x **0.5)+1):
#         if x %i == 0:
#             break
#     else:
#         Prime.append(x)
# print(Prime)

# import math
# Prime = []
# n = 100
# for x in range(2, n):
#     for i in range(2, math.ceil(math.sqrt(x))):
#         if x % i == 0:
#             break
#     else:
#         Prime.append(x)
# print(Prime)

# import math
# n = 100
# Prime = []
# for x in range(2, n):
#     for i in Prime:
#         if x % i == 0:
#             break
#     else:
#         Prime.append(x)
# print(Prime)

# import math
# Prime = []
# flag = False
# for x in range(2, 100):
#     for i in Prime:
#         if x % i ==0:
#             flag = True
#             break
#         if i >= math.ceil(math.sqrt(x)):
#             flag = False
#             break
#     if not flag:
#         Prime.append(x)
# print(Prime)

# 计算杨辉三角前6行

# triangle = [[1], [1,1]]
# for i in range(2, 6):
#     cur = [1]
#     pre = triangle[i-1]
#     for j in range(len(pre)-1):
#         cur.append(pre[j]+pre[j+1])
#     cur.append(1)
#     triangle.append(cur)
# print(triangle)

# triangle = []
# n = 6
# for i in range(n):
#     row = [1]
#     triangle.append(row)
#     if i == 0:
#         continue
#     for j in range(i-1):
#         row.append(triangle[i-1][j]+triangle[i-1][j+1])
#     row.append(1)
# print(triangle)

# n = 6
# oldline = []
# newline = [1]
# length = 0
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     offset = 0
#     while offset <= i:
#         newline.append(oldline[offset-1] + oldline[offset])
#         offset += 1
#     print(newline)

# n = 6
# oldline = []
# newline = [1]
# lenght = 0
# print(newline)
# for i in range(1, n):
#     oldline = newline.copy()
#     oldline.append(0)
#     newline.clear()
#     for j in range(i+1):
#         newline.append(oldline[j-1]+oldline[j])
#     print(newline)

# triange = []
# n = 6
# for i in range(n):
#     row = [1]
#     for k in range(i):
#         row.append(1) if k == i-1 else row.append(0)
#     triange.append(row)
#     if i == 0:
#         continue
#     for j in range(1, i//2+1):
#         val = triange[i-1][j-1] + triange[i-1][j]
#         row[j] = val
#         if j != i-j:
#             row[-j-1] = val
# print(triange)

triangle = []
n = 6
for i in range(n):
    row = [1]*(i+1)
    triangle.append(row)
    if i == 0:
        continue

    for j in range(1,i//2+1):
        var = triangle[i-1][j-1] + triangle[i-1][j]
        row[j] = var
        if i != 2j:
            row[-j-1] = var
print(triangle)