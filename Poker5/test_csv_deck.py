# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习使用 csv 文件写一副牌
# ------------------------(max to 80 columns)-----------------------------------

from machine.std_mach import *


deck = []
create_deck_52(deck)
record_deck_csv(deck, '52张扑克牌.csv')

deck = []
create_deck_54(deck)
record_deck_csv(deck, '54张扑克牌.csv')

deck = []
read_deck_csv('52张扑克牌.csv', deck)
print('--debug 52 deck: \n%s' % (deck))

deck = []
read_deck_csv('54张扑克牌.csv', deck)
print('--debug 54 deck: \n%s' % (deck))
