#!/usr/bin/env python3

with open('numbers1.txt', 'r') as inputeFile:
    content = inputeFile.read()
    contents = content.split()
    
    mean = 0
    for i in contents:
        number = float(i)
        mean = mean + number
    print(mean)
