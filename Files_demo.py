# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:23:51 2020

@author: msingh31
"""

#Reading from text file

file1 = open('new.txt','r')
file1.read()
file1.close()

#Writing into text file.
file1 = open('new.txt','w')
file1.write('I love ML')
file1.close()

#Appending text file.
file1 = open('new.txt','a')
file1.write('\nHello World')
file1.close()

#creating new text file and write
file1 = open('new1.txt','w+')
file1.write('I love ML')
file1.close()

#reading multiple lines from text file
file1 = open('newdemo.txt','r')
x = file1.readline()
print(x)
file1.close()

file1 = open('newdemo.txt','r')
x = file1.readlines()
for e in x:
    print(e)
file1.close()

#Copying file1 to file2 
file1 = open('8.jpg','rb')
file2 = open('Mypic.jpg','wb')
for i in file1:
    file2.write(i)
file2.close()
file1.close()


import pandas as pd
dir(pd)

import sys
sys.version
sys.version_info







