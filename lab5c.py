#!/usr/bin/env python3
# Author ID: bjpatel18

def add(number1, number2):
    try:
        n1 = int(number1)
        n2 = int(number2)
        return n1 + n2
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))
    print(add('10',5))
    print(add('abc',5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
