# -*- encoding=utf8 -*-
# 一摞Python风格的纸牌

import collections
from random import choice
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()  # spades表示黑桃，diamonds表示方块，
    # clubs表示梅花，hearts表示红心
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  # 黑桃最大，红桃次之，方块再次，梅花最小

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):  # 定义该函数后，就可以对 类 FrenchDeck使用 len()函数
        return len(self._cards)

    # 这个类的实现存在问题，FrenchDeck 的切片是 list 类型，而不是 FrenchDeck 类型
    def __getitem__(self, position):  # 可以以索引（下标）的方式对FrenchDeck的元素进行引用：1、可切片；2、可迭代；
        # 3、可使用 random.choice()函数;3、可以使用 in 运算符
        return self._cards[position]

    # def __setitem__(self, key, value): # 实现该方法，可以轻松地实现洗牌功能
    # 	self._cards[key] = value

    def spades_high(card):  # 黑桃最大
        rank_value = FrenchDeck.ranks.index(card.rank)

        return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]


if __name__ == '__main__':
    frenchDeck = FrenchDeck()

    print(len(frenchDeck))
    print(frenchDeck[0])
    print(frenchDeck[12::13])  # 切片[start:end:step]

    # 正向迭代
    for card in frenchDeck:
        print(card)

    # 反向迭代
    for card in reversed(frenchDeck):
        print(card)

    # 使用 in 运算符
    if Card('K', 'diamonds') in frenchDeck:
        print('Card("K", "diamonds")', '在 frenchDeck 中')

    # 根据 规则spades_high 进行排序
    for card in sorted(frenchDeck, key=FrenchDeck.spades_high, reverse=True):
        print(card)

    print(choice(frenchDeck))  # 随机抽取一张牌


    # 下面的代码打上猴子补丁

    def set_card(deck, pos, card):
        deck._cards[pos] = card


    FrenchDeck.__setitem__ = set_card

    # 洗牌
    random.shuffle(frenchDeck)
    print(frenchDeck[:5])