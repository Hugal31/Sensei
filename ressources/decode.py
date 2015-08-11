#!/usr/bin/env python3

letter = input('Choose a character : ')
for i in letter:
    print(i, ord(i), '0x%x' % ord(i))
