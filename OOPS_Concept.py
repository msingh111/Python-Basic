# OOPS Concept in Python

class comp1:
    print('G3 HP Comp')
    
c1 = comp1()


# class with fruntions with 1 object
class comp:
    def config(self):
        print('i5, 16GB, 1TB')

c1 = comp() # c1 is oject of comp class
c1.config() # object.method
comp.config(c1) # class name. methodname(objet)

## class with fruntions with multiple object 
class compu:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print('Config is: ',self.cpu, 'and RAM is: ', self.ram)

c1 = compu('i5',8) # c1 is oject of comp class
c2 = compu('i7',16)
c1.config() # object.method
c2.config()

# Constructor in Python
class compu:
    def __init__(self):
        self.name = 'Munijee'
        self.age = 30    
    
    def update(self):
        self.age = 28
    
    def compare(self,other):
        if self.age==other.age:
            return True
        return False
        
c1 = compu() # all oject stored in Head memory 
c2 = compu()

c1.name = 'Dolly'
c1.update()

if c1.compare(c2):
    print('Same Age')
else:
    print('Diff Age')

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)


# Variable in OOPS python
class car:
    
    wheels = 4 # Class variable 
    
    def __init__(self):
        self.mil = 10 # in side __init variable are called instance variable
        self.com = 'BMW'

c1 = car()
c2 = car()

c2.mil = 8
car.wheels = 5


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)




# Diff methods in OOPS python
class student:
    
    school = 'SRM'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self): #instant methong 
        return (self.m1+self.m2+self.m3)/3
        
    def get_m1(self):
        return self.m1
    
    def set_m1(self, v):
        self.m1 = v
    
    @classmethod # Class method
    def getschool(cls):
        return cls.school
    
    @staticmethod # Static method
    def info():
        print('This is static method')

s1 = student(56,76,39)
s2 = student(94,39,67)

s1.avg()
s2.get_m1()
s1.set_m1(34)

s1.get_m1()
student.info()
s1.info()



# Inner class (Class within class)
class stu:
    
    
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
    def show(self):
        print('Name: ',self.name,', Roll: ',self.roll)
        
        
        
    class laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
        
s1 = stu('Munijee',2)
s2 = stu('Dolly',4)
l1 = stu.laptop()

s1.show()
s2.show()
l1.show()


#Inheritance concept in Python
class a:
    
    def feature1(self):
        print('Featre 1 working')
    
    def feature2(self):
        print('Featre 2 working')


class b(a):
    
    def feature3(self):
        print('Featre 3 working')
    
    def feature4(self):
        print('Featre 4 working')

class c(b):
    def feature5(self):
        print('Featre 3 working')
        
        
a1 = a()
a1.feature1()
a1.feature2()

b1 = b()
b1.feature3()
b1.feature1()

c1 = c()


#Multople inheritance
class a1:
    
    def feature1(self):
        print('Featre 1 working')
    
    def feature2(self):
        print('Featre 2 working')


class b1():
    
    def feature3(self):
        print('Featre 3 working')
    
    def feature4(self):
        print('Featre 4 working')

class c1(a1,b1):
    def feature5(self):
        print('Featre 5 working')
        
        
a = a1()
a.feature1()

b = b1()
b1.feature3()

c = c1()
c.feature3()
c.feature1()
c.feature5()


# Construction in inheritance
class a2:
    
    def __init__(self):
        print('in A2 init')
    
    def feature1(self):
        print('Featre 1-A working')
    
    def feature2(self):
        print('Featre 2-A working')


#class b2(a2):
class b2:    
    def __init__(self):
        #super().__init__()
        print('in B2 init')
    
    def feature1(self):
        print('Featre 1-B working')
    
    def feature2(self):
        print('Featre 1-B working')

class c2(a2,b2):
    def __init__(self):
        super().__init__() # In multiple inheritance super always work from lef
        print('in c2 init')
    
    def met(self):
        super().feature1()

b = c2()
b.met()



#polymorphism in Python
"""
Poly = Many
morph = Form

>> Duck Typing
>> Operator overloading
>> method overloading
>> method overridding
"""

#Duck typing in Pythond
class Spyder:
    def execute(self):
        print('Compiling')
        print('Running')

class pycharm:
    def execute(self):
        print('Spell checking')
        print('Auto Correct')

class lap:
    
    def code(self, ide):
        ide.execute()

ide = Spyder()
ide1 = pycharm()
l1 = lap()

l1.code(ide1)


#Operator overloading
class student:
    
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        
        s3 = m1 + m2
        return s3
    
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        
        if s1 > s2:
            print('S1 Win')
        else:
            print('S2 Win')
            
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
        #return self.m1, self.m2
        
        
s1 = student(55,68)
s2 = student(95,63)

s3 = s1 + s2           #student.__add__(s1+s2)
print(s3)

s1>s2

#print(s1.__str__())
print(s1)
print(s2)


# Operator overloading
"""
1. Method overloading - Python does not support
2. Method overriding

"""

class student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
   
    def sum(self, a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

    
s1 = student(65,49)
print(s1.sum(4,5,12))
print(s1.sum(3,9))


#Method overriding
class dem:
    
    def show(self):
        print('In A show')

class dem1(dem):
    def show(self):
        print('In B show')

d = dem()
d1 = dem1()
d.show()
d1.show()















































































































































































