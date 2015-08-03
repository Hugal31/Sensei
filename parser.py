#!/usr/bin/env python3
## parser.py for parser in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 14:50:36 2015 Hugo Laloge
## Last update Mon Aug  3 15:05:55 2015 Hugo Laloge
##

import re

re_comment = re.compile('\s*#')
re_data = re.compile('(\S+):(\S+)')

# Parse un fichier avec des equivalences x:y
def parser(file_name):
    global re_comment, re_data
    data=[]
    fd = open(file_name)
    for line in fd.readlines():
        if re.match(re_comment, line):
            None
        elif re.search(re_data, line):
            data.append(re.findall(re_data, line)[0])
    return data
