#!/usr/bin/env python3
## remember.py for Remember Hiragana in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 13:13:03 2015 Hugo Laloge
## Last update Mon Aug  3 15:19:13 2015 Hugo Laloge
##

from os import system
from sys import argv
from random import randint
from parser import parser

class Teacher:
    def __init__(self, file_name):
        self.dictionary = parser(file_name)

    # Demande une fois chaque kana et donne le score
    def exam(self):
        score = 0
        rate = len(self.dictionary)
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            syllabe = self.dictionary[index]
            if (self.ask(syllabe)):
                score += 1
            self.dictionary.pop(index)
        system('clear')
        print ('Score : %d/%d' % (score, rate))
        return score / rate

    # Demande chaque kana jusqu'a que on ai donné la bonne réponse à tous
    def teach(self):
        score = 0
        rate = len(self.dictionary)
        while len(self.dictionary) != 0:
            index = randint(0, len(self.dictionary) - 1)
            syllabe = self.dictionary[index]
            if (self.ask(syllabe)):
                score += 1
                self.dictionary.pop(index)
        print ('Finish !')

    def ask(self, syllabe):
        response = input('What do %s meen ? : ' % (syllabe[1]))
        if (response == syllabe[0]):
            print ('Correct !')
            return True
        else:
            print('Incorrect, it was %s' % (syllabe[0]))
            return False

if __name__ == '__main__':
    if (len(argv) > 1):
        teacher = Teacher(argv[1])
    else:
        teacher = Teacher('ressources/hiragana.txt')
    teacher.exam()
