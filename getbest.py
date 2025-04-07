#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    i=1
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i+1
    return (num_col, mark_col)


def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = 0
    best_idx = 0
mark = int(data[num_col]) ''' the actually mark oin the mark column'''
num = int(data[num_col])''' the actually student number in the column'''
        if mark > best:
            best=mark '''updating the best mark'''
            best_idx=num '''updating the student number after best is found'''
    return best_idx, best
'''Printing the result in the correct format'''
f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))
