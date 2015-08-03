#!/usr/bin/env python3
## sensei.py for Sensei in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 13:13:03 2015 Hugo Laloge
## Last update Mon Aug  3 17:08:10 2015 Hugo Laloge
##

import argparse
from os import system
from random import randint
import re
import sys

from parser import parser

re_response_alpha = re.compile('\w{1,3}')

class Sensei:
    def __init__(self, files):
        self.dictionary = []
        for file in files:
            self.dictionary += parser(file)

    # Demande une fois chaque kana et donne le score
    def exam(self):
        score = 0
        rate = len(self.dictionary)
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            equivalence = self.dictionary[index]
            if (self.ask(equivalence)):
                score += 1
            self.dictionary.pop(index)
        print ('Score : %d/%d' % (score, rate))
        return score / rate

    # Demande chaque kana jusqu'a que on ai donné la bonne réponse à tous
    def teach(self):
        score = 0
        rate = len(self.dictionary)
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            equivalence = self.dictionary[index]
            if (self.ask(equivalence)):
                score += 1
                self.dictionary.pop(index)
        print ('Finish !')

    def ask(self, equivalence):
        good=False
        while not good:
            response = input('What do %s mean ? : ' % (equivalence[1]))
            good = re.fullmatch(re_response_alpha, response)
            if not good:
                print ('Try again !')
        if (response == equivalence[0]):
            print ('Correct !')
            return True
        else:
            print ("Incorrect, it was '%s'" % (equivalence[0]))
            return False

def arg_parse():
    parser = argparse.ArgumentParser(description=
                                     """Programme pour apprendre les kana et les kanji""")

    parser.add_argument('--mode',
                        default='exam',
                        choices=['exam', 'teach'],
                        type=str,
                        help='Mode d\'enseignement')

    parser.add_argument('files',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Le fichier dictionnaire')

    return parser.parse_args()

if __name__ == '__main__':
    args = arg_parse()
    sensei = Sensei(args.files)
    if (args.mode == 'exam'):
        sensei.exam()
    else:
        sensei.teach()
