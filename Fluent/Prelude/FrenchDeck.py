# -*- encoding=utf-8 -*-

"""
author: Adler Liu(刘德涵)
url: https://adlerliu.me
copyright: © 2018 Adler Liu
license: MIT, see LICENSE for more details.
"""

# 一摞Python风格的纸牌
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]


# 我们用collections.namedtuple构建一个简单的类表示一张纸牌
# 利用namedtuple，得到一个纸牌对象
beer_card = Card('7', 'diamonds')
print(beer_card)

# 查看多少张牌
deck = FrenchDeck()
print(len(deck))

# 抽出特定的一张纸牌，这个方法是有__getitem__提供
print(deck[0])  ## 第一张纸牌，根据索引来抽取
print(deck[-1])  ## 最后一张纸牌

# 随机抽取纸牌
from random import choice

print(choice(deck))
print(choice(deck))

# 应为__getitem__方法把[]操作交给了self._cards列表，所以deck类自动支持切片
print(deck[:3])  # 最上面三张牌
print(deck[12::13])  # 先拿索引12的牌，然后隔13拿一张

# 仅仅实现__getitem__方法，可以实现迭代

# 正向迭代
for card in deck:
    print(card)

# 反向迭代
for card in reversed(deck):
    print(card)

# 实现__contains__方法，那么in运算符就能进行迭代搜索
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# 进行排序
suit_valuse = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spads_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_valuse) + suit_valuse[card.suit]


# 有了spads_high函数，就能对牌进行排序
for card in sorted(deck, key=spads_high):
    print(card)
