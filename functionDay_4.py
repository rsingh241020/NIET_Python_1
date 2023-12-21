#def Sum_number():
 #   a=10
 #   b=20
 #   print(a+b)


#Sum_number()
    
#def Sum_number():
#    a = int(input("Enter a number"))    
#    b = int(input ("Enter b Number"))
#    print(a+b)
    
#Sum_number()

#1st Type
'''def fib_ser():
    number = int(input("Enter a  number for Fibonacci... :  "))
    num1 = 0
    num2 = 1
    next_number = num1  
 
    for i in range (number):
        print(next_number, end=" ")
        num1, num2 = num2, next_number   
        next_number = num1 + num2

fib_ser()

'''

#2nd Type
'''
def sum_num():
    a = 10
    b = 20
    c = a + b
    return c

a = sum_num()
print(a)
'''
#3rd Type
#def add(num1,num2):
#    c = num1+num2
#    print(c)
#add(567,68)


#4th Type
'''def add(a,b):
    c=a+b
    return c
d=add(23,232)
print(d)
print(add(10,5))
'''

def add(a=2,b=10):
    c=a+b
    return c
d=add(2)
print(d)

