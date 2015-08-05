#!/usr/bin/env python3
## sensei.py for Sensei in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 13:13:03 2015 Hugo Laloge
## Last update Wed Aug  5 15:22:28 2015 Hugo Laloge
##

import argparse
from os import system
from random import randint
import re
import sys
from time import time
import tkinter

from parser import parser

re_response_alpha = re.compile('\S.*')

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
            response = input('What do %s mean ? : ' % ('|'.join(equivalence[1])))
            good = re.fullmatch(re_response_alpha, response)
            if not good:
                print ('Try again !')
        if (response in equivalence[0]):
            print ('Correct !')
            return True
        else:
            print ("Incorrect, it was '%s'" % ('|'.join(equivalence[0])))
            return False

    def response(self):
        char = input('Which one ? : ')
        for equivalence in self.dictionary:
            if char in equivalence[0]:
                print ('->', '|'.join(equivalence[1]))
                return equivalence[1]

class SenseiGui(Sensei):
    def __init__(self, files):
        super().__init__(files)
        self.window = tkinter.Tk()

        self.label = tkinter.Label(self.window, width=4, height=1, text='toto', font='TakaoMincho 74')
        self.label.pack()

        self.message = tkinter.Label(self.window, width=40, height=1, font='sans-serif 15')
        self.message.pack()

        self.entry = tkinter.Entry(self.window, width=20, font='sans-serif 15')
        self.entry.bind('<Return>', self.get_answer)
        self.entry.pack()

        self.button = tkinter.Button(self.window, command=self.get_answer, text='Enter')
        self.button.pack()

    def exam(self):
        self.mode = 'exam'
        self.score = 0
        self.rate = len(self.dictionary)
        self.start_time = time()
        self.ask_random()
        self.window.mainloop()

    def ask_random(self):
        if len(self.dictionary) == 0:
            print_score(self.score, self.rate, self.start_time)
            exit()
        self.current_index = randint(0, len(self.dictionary) - 1)
        self.ask(self.dictionary[self.current_index])

    def ask(self, equivalence):
        self.label.config(text=equivalence[1][0])

    def get_answer(self, garbage):
        answer = self.entry.get()
        if answer in self.dictionary[self.current_index][0]:
            self.score += 1
            self.message.config(text='Correct !')
        else:
            self.message.config(text='Incorrect, it was \'%s\'' % '|'.join(self.dictionary[self.current_index][0]))
        if self.mode == 'exam':
            self.dictionary.pop(self.current_index)
        self.entry.delete(0, len(self.entry.get()))
        self.ask_random()


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

    parser.add_argument('-g,--gui',
                        const=True,
                        dest='gui',
                        nargs='?',
                        help='Mode graphique')

    return parser.parse_args()

if __name__ == '__main__':
    args = arg_parse()
    if args.gui:
        sensei = SenseiGui(args.files)
    else:
        sensei = Sensei(args.files)
    if args.mode == 'exam':
        sensei.exam()
    elif args.mode == 'teach':
        sensei.teach()
    else:
        sensei.response()
