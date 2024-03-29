#!/usr/bin/env python3
## parser.py for parser in /home/laloge_h/Documents/Japonais
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Mon Aug  3 14:50:36 2015 Hugo Laloge
## Last update Sat Aug  8 09:25:09 2015 Hugo Laloge
##

import re

re_comment = re.compile('\s*#')
re_data = re.compile('(.+):(.+)')
re_end = re.compile('__END__')

# Parse un fichier avec des equivalences x:y
def parser(fd):
    global re_comment, re_data
    data=[]
    for line in fd.readlines():
        if re.match(re_comment, line):
            None
        elif re.search(re_data, line):
            equivalence = ['', '']
            equivalence[0] = re.findall(re_data, line)[0][0].split('|')
            equivalence[1] = re.findall(re_data, line)[0][1].split('|')
            data.append(equivalence)
        elif re.match(re_end, line):
            return data
    return data
