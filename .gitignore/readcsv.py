# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:24:48 2020

@author: Harish
"""

import csv

with open('leaf.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,dialect='excel')
    for row in reader:
        print(row)

csvFile.close()

