# lamba Function

'''x = lambda :print("Hello")
print(x())
print(type(x))
'''
'''
y = lambda a,b :a+ 10
print(y(5,5))'''

'''
y = lambda a,b :a **b
print(y(5,2))
'''
'''y = lambda a,b,c :a+b+c
print(y(5,5,4))
'''
x = lambda : lambda a: a+10
print(x())
