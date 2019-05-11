# -*- encoding=utf-8 -*-
# 在字典中将键映射到多个值上

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

d = {}
for key, value in d:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

d = defaultdict(list)
for key, value in d:
    d[key].append(value)
print(d)

