# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:57:22 2020

@author: msingh31
"""

# Exception Handling
a,b = 5,2
a/b
try:
    print(a/b)
except Exception as e:
    print('Can not divide by zero',e)
finally:
    print('Hello world')


# Exception handing by error name
try:
    print(a/b)
except ZeroDivisionError as e:
    print('Can not divide by zero:',e)
except NameError as e:
    print(e)
except TypeError as e:
    print('Please enter numbers only:',e)
finally:
    print('Operation completed')



















