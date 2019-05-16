# -*- encoding=utf-8 -*-
# 对序列使用+和*
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

# 建立由列表组成的列表
## 一个包含3个列表的列表，嵌套的3个列表各自有3个元素来代表井字游戏的一行方块
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'x'
print(board)

# 含有3个指向同一对象的引用的列表是毫无用处的
weird_board = [['_'] *3] *3
print(weird_board)

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
board[2][0] = 'x'
print(board)

# 序列的增量赋值
l = [1, 2, 3]
print(id(l))
l *= 2
print(l, id(l))
t = (1, 2, 3)
print(id(t))
t *= 2
print(t, id(t))

# 一个谜题
t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)

# 没人料到结果，t[2]被改动了，但有异常抛出
t = (1, 2, [30, 40])
t[2] += [50, 60]
print(t)

