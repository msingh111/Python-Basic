#__name__ example

def add(a,b):
    print('Sum: ',a+b)

def sub(a,b):
    print('Substraction: ',a-b)
    #print(__name__)
    
def mul(a,b):
    print('Multiplication: ',a*b)

def div(a,b):
    print('Divide: ',a/b)

a = 9
b = 7

if __name__ == '__main__':
    def main():
        add(a,b)    
        sub(a,b)
        mul(a,b)
        div(a,b)
    main()
