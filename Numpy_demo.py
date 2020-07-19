#numpy in python
"""
Similarity: Storing Data, Mutable, can be indexed and slicing operation
Differance: List - Differnet Datatype where in Array - Similar Datatype
            arithmatic operation is not posstible on list where we can perform operation on Array
            list is built in function where numpy is addon library
Advantages: Numpy- Use less memory, Fast and more convenient


1. Array
2. Arange
3. Zero
4. Ones
5. Linspace
6. Identity
7. Eys
8. Random
"""

import numpy as np
#Numpy usin array
arr = np.array([1,2,4,5,6])
print(arr)
arr.size
arr.shape
arr.ndim
arr.itemsize
arr.dtype

#numpy using Arange
arr1 = np.arange(1,10)
arr1

#Numpy using Linspace
arr2 = np.linspace(1,10,10)
arr2.astype('int')

#numpy using zeros
arr3 = np.zeros([2,3], dtype='i', order = 'c')
arr3

#numpy using ones
arr4 = np.ones([3,3],dtype='int')
arr4

#Numpy using identity
arr5 = np.identity(3)
arr5

#numpy using eye
arr6 = np.eye(3,k=-1)
arr6

#Numpy using Randon function
arr7 = np.random.rand(2,3)
arr7

arr8 = np.random.randint(1,20,size=[2,3])
arr8

arr9 = np.random.randint([1,5,7],10)
arr9

arr10 = np.random.randint([1,5,7,3],[[10],[20]])
arr10


#Arithmatic operation on numpy
#Using numpy function
np.add(arr1,2)
np.subtract(arr1,1)
np.multiply(arr1,2)
np.divide(arr1,2)
np.mod(arr1,2)
np.square(arr1)
np.sqrt(arr1)

#using Arithmatic sign
arr1+2
arr-1
arr1*2
arr1/2
arr1%2
arr1**2


#Numpy reshape and resize
print(arr2)
arr2.shape
arr2.reshape([5,2])

#Appending Numpy array
arr1 = np.append(arr1,[2,4,6,8], axis=0)

x = np.arange(1,10)
x.reshape(3,3)
x.reshape(9,1)
x.reshape(1,9)
np.resize(x,(3,4))
np.reshape(x,(3,3))


#Slicing in numpy
dem = np.random.randint(1,20,size=(5,5))
dem[1:3,:]
dem[::2,:]
dem[::2,::2]
dem[-3:-1,::2]
dem[-1,]


#Coping Numpy array
a = np.array([1,3,5,6,7])
b = a
print(id(a))
print(id(b))
print(a)
print(b)

c = a.view()
print(id(a))
print(id(c))
print(c)
print(a)

d = a.copy()
print(id(a))
print(id(d))
print(d)
print(a)

d1 = a+2
print(d1)
print(d)

d+d1

a[3]=4


#Numpy concatination
con1 = np.zeros([3,3])
con2 = np.ones([3,3])
np.concatenate([con1,con2],axis=0)
np.concatenate([con1,con2],axis=1)

#stacking
np.vstack([con1,con2])
np.hstack([con1,con2])

#__Row__Col
np.r_[con1,con2]
np.c_[con1,con2]


#Flatarn and Ravel
c_falt = con2.flatten()
c_rav = con2.ravel()
print(c_falt)
print(c_rav)

c_rav[4]=2
con2
con2[1,1]=4


arr.max()
arr.mean()
arr.argmax()
arr.argmin()
arr.cumsum()
arr.sum()

#Where with numpy
arr[np.where(arr>3)]
dem[np.where(dem>=14)].reshape(4,2)


















