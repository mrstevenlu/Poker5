# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   定义标准发牌机的动作函数
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls

from binascii import b2a_hex, a2b_hex
import random
import codecs
import os
import rsa

# Poker 4.0 added
import csv
import logging

global app_name
app_name = 'test_log'
logger = logging.getLogger(app_name)


def create_deck_54(new_deck):
    '推出一副54张的新牌'

    # initialize var
    cardJokers = ('♞', '♘')
    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    # Poker 4.0 added
    msg = '推出了一副54张的新扑克牌'
    logger.info(msg)

    return


def create_deck_52(new_deck):
    '推出一副52张的新牌'

    cardMarks = ('♠', '♥', '♣', '♦')
    cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    # add 4x13 cards
    for cm in cardMarks:
        for cn in cardNumbers:
            card = cm + cn
            new_deck.append(card)

    # Poker 4.0 added
    msg = '推出了一副52张的新扑克牌'
    logger.info(msg)

    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'

    random.shuffle(deck_to_be_shuffled)
    # Poker 4.0 added
    msg = '洗了下牌'
    logger.info(msg)

    return


'''
def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n -- debug: I record a deck')

    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    # print(out_path)
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close

    return
'''

# ---- Poker 3.0 added and Poker 4 updated


def make_deck_by_type(play_type, out_deck):
    '按要求制作各种扑克牌'

    '''
    if play_type == 1:  # 争上游的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '争上游-刚洗好的牌.txt')
    if play_type == 2:  # 桥牌
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '桥牌-刚洗好的牌.txt')
    if play_type == 3:  # 三人斗地主的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck(out_deck, '三人斗地主-刚洗好的牌.txt')
    if play_type == 4:  # 四人斗地主的牌
        # first deck
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        # second deck
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        # shuffled & record
        shuffled_deck(out_deck)
        record_deck(out_deck, '四人斗地主-刚洗好的牌.txt')
    '''

    # ---- Poker 4.0 added
    if play_type == 1:  # 争上游的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '争上游-刚洗好的牌.csv')
    elif play_type == 2:  # 桥牌
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '桥牌-刚洗好的牌.csv')
    elif play_type == 3:  # 三人斗地主的牌
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '三人斗地主-刚洗好的牌.csv')
    elif play_type == 4:  # 四人斗地主的牌
        # first deck
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        # second deck
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        # shuffled & record
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '四人斗地主-刚洗好的牌.csv')
    else:
        msg = '无法识别的游戏类型 (%d)' % (play_type)
        logger.error(msg)

    return

# ---- Poker 4.0 added



def record_deck_csv(deck_to_be_record, csv_filename):
    '用CSV格式记录一副牌'

    csv_path = os.getcwd() + '\\csv_decks\\' + csv_filename

    with open(csv_path, "w", encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(deck_to_be_record)

    # Poker 4.0 added
    msg = '把牌的内容记录到了文件 (%s)' % csv_path
    logger.debug(msg)

    return
'''
def read_deck_csv(csv_filename, out_deck):
    '读取 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_decks\\' + csv_filename
    with open(in_path, "r", encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            out_deck.extend(line)

    # Poker 4.0 added
    msg = '从文件 (%s) 中读取了牌的内容' % in_path
    logger.debug(msg)

    return
'''


def record_deck_crypted_csv(deck_to_be_record, csv_filename, public_key):
    csv_path = os.getcwd() + '\\csv_decks\\crypted_' + csv_filename
    joined_deck = ','.join(deck_to_be_record)
    row_data = rsa.encrypt(joined_deck.encode(), public_key)
    row_data = b2a_hex(row_data)

    f = open(csv_path, 'wb')
    f.write(row_data)
    f.close()

    return


def read_deck_crypted_csv(csv_filename, out_deck, private_key):
    '读取加密过的 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_decks\\crypted_' + csv_filename
    f = open(in_path, 'rb')
    line = f.read()
    f.close()

    s = a2b_hex(line)
    row_data = rsa.decrypt(s, private_key)
    #print('--debug: read from csv file : %s' % row_data.decode())
    s = row_data.decode()
    out_deck.extend(s.split(','))
    print(out_deck)

    return
