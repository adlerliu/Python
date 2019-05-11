# -*- encoding=utf-8 -*-

# 实现优先级队列
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
print(q.push(Item('foo'), 1))
print(q.push(Item('bar'), 5))
print(q.push(Item('spam'), 4))
print(q.push(Item('grok'), 1))

a = (1, Item('foo'))
b = (5, Item('bar'))
if a < b:
    print(1)
    