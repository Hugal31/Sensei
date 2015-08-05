#!/usr/bin/env python3
## sensei.py for Sensei in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 13:13:03 2015 Hugo Laloge
## Last update Tue Aug  4 11:12:54 2015 Hugo Laloge
##

import argparse
from os import system
from random import randint
import re
import sys
from time import time

from parser import parser

re_response_alpha = re.compile('\w{1,3}')

def print_score(score, rate, start_time):
    print ('Score : %d/%d'  % (score, rate))
    print ('Ratio : %0.2f' % (score / rate))
    print ('Time : %dm%ds' % (int((time() - start_time) / 60), (time() - start_time) % 60))
    print ('Time / character : %.1fs' % ((time() - start_time) / rate))

class Sensei:
    def __init__(self, files):
        self.dictionary = []
        for file in files:
            self.dictionary += parser(file)

    # Demande une fois chaque kana et donne le score
    def exam(self):
        score = 0
        rate = len(self.dictionary)
        start_time=time()
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            equivalence = self.dictionary[index]
            if (self.ask(equivalence)):
                score += 1
            self.dictionary.pop(index)
        print_score(score, rate, start_time)
        return score / rate

    # Demande chaque kana jusqu'a que on ai donné la bonne réponse à tous
    def teach(self):
        score = 0
        rate = len(self.dictionary)
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            equivalence = self.dictionary[index]
            if (self.ask(equivalence)):
                self.dictionary.pop(index)
            else:
                score -= 1
        print ('Finish !')
        print ('You made %d errors' % (score))

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

    def response(self):
        char = input('Which one ? : ')
        for equivalence in self.dictionary:
            if char == equivalence[0]:
                print ('-> ', equivalence[1])
                return equivalence[1]

def arg_parse():
    parser = argparse.ArgumentParser(description=
                                     """Programme pour apprendre les kana et les kanji""")

    parser.add_argument('--mode',
                        default='exam',
                        choices=['exam', 'teach', 'question'],
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
    if args.mode == 'exam':
        sensei.exam()
    elif args.mode == 'teach':
        sensei.teach()
    else:
        sensei.response()
