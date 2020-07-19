# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:18:34 2020

@author: msingh31
"""

#Generator
'''
def gen():
    i = 1
    while i <= 10:
        sq = i*i
        yield sq
        i+=1

x = gen()
count = 1
for i in x:
    print('Sqrt of ',count,' is: ',i)
    count +=1
    if count==4:
        break

#iterator
name =[3,5,7,12]
i = iter(name)
print(next(i))
print(i.__next__())
'''
class topten:
    x = 0
    def __init__(self,num):
        self.num = num
        self.it = 1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.it <= 10:
            val = self.num
            global x
            x +=val
            self.it+=1
            return x
        else:
            raise StopIteration

ten = topten(13)
x = 0
for i in ten:
    print(i)
    

'''
#Decoder
def decor(abc):
    def wrapper():
        print('Decor')
        x = abc()
        #print(type(x))
        x = x+4
        return x
    return wrapper

def decor1(ab):
    def wrapper():
        print('Decor1')
        x = ab()
        x = x+3
        return x
    return wrapper

def decor2(ab):
    def wrapper():
        print('Decor2')
        x = ab
        x = x+2
        return x
    return wrapper


def sum(a,b):
    c = a+b
   # print('Hello')
    return c

#fin = decor(sum(5,4))
#fin1 = decor1(sum(5,4))
fin = decor(decor1(decor2(sum(4,5))))
print(fin())
#print(fin1())



def dec(x):
    def wrapper():
        print('Before Wrapper')
        x()
        print('World')
    return wrapper

@dec
def dem():
    x = 5 + 10
    print(x)

#f = dec(dem())
dem()

'''














