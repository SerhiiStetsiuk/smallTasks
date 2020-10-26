#!/usr/bin/env python3

with open('numbers1.txt', 'r') as inputeFile:
    sum = 0
    for line in inputeFile:
        if not line.startswith("#"):
            contents = line.split()
            for l in contents:
                number = float(l)
                sum = sum + number      
    print("summa = ", sum)