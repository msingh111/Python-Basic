# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:41:02 2020

@author: msingh31
"""

# Function in python

#Simple Function Expample
def demo():
    print('Hello Advit')
    print('Good Morning')

demo()

#function with argument (Position wise)
def person(name,age):
    print(name)
    print(age)

person('Advit',4)

#function with argument (Default Value)
def person1(name,age=6):
    print(name)
    print(age)

person1('Advit',4)

#function with argument (Sequance)
def person2(name,age):
    print(name)
    print(age)

person2(age=4, name='Advit')

#Function with argument (*Infinite Argument)
def add(x,*y):
    c = x
    for i in y:
        c = c+i
    print(c)

add(2,3,5)

#Function with argument (**Infinite Argument)
def person3(name,**dtl):
    print('name :',name)
    for i,j in dtl.items():
        print(i,':',j,end="\n")


person3(name='Advit',age=4,city='Noida',clas='Nursary')

#Function retuning multiple values
def calc(x,y):
    a = x+y
    b = x-y
    return a,b

x,y = calc(8,5)
print(x)
print(y)

#Passig list to a function
def odd_even(lst):
    o=[]
    e=[]
    for i in lst:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)   
    print('Odd numbers are: ',o)
    print('Even numbers are: ',e)

lst = [1,3,4,5,7,8,9,10,12]
odd_even(lst)

































