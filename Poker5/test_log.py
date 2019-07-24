# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习用 logging 模块
# ------------------------(max to 80 columns)-----------------------------------


import logging
import os

from machine.std_mach import *

# 定义了 logger 的名字
global app_name
app_name = 'test_log'
logger = logging.getLogger(app_name)

# 定义了 logger 的输出形式
log_path = os.getcwd() + '\\log_files\\' + app_name + '.log'
logging.basicConfig(level=logging.DEBUG,
                    filename=log_path,
                    format='%(asctime)s - %(levelname)s : %(name)s - %(filename)s -%(funcName)s() -No.%(lineno)d - %(message)s')

# 调用其他模块，测试 log 是否正常工作
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

deck = []
make_deck_by_type(4,deck)
