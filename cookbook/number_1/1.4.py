# -*- encoding=utf-8 -*-

# 找到最大或最小的N个元素
# import heapq

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3,nums))

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'APPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
#
# print(cheap)
# print(expensive)

# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# import heapq
#
# heap = list(nums)
# heapq.heapify(heap)  //从小到大排列
# print(heap)
#
# heapq.heappop(heap)
# print(heap)
# heapq.heappop(heap)
# print(heap)
# heapq.heappop(heap) //最小的弹出
# print(heap)

