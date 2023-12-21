#list1 = [1,2,3,4,[3,4,5],34,42,23]
#
'''list1 = [[1,2,3,],
         [4,5,6],
         [7,8,9]]
print(list1)
for i in range(3):
    for j in range(3):
        print(list1[i][j],end=" ")
    print()
'''
'''l =list(input("Enter List: ").split())# workig as a string-
print(l)
'''
#print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!=y])
'''a = 3.0
b = 3
c=3.0000
print(a==b==c)
'''

# Tuple
'''

#tuple1 =(1,2,3,'harsh',4.5)
#print(tuple1)
#t= tuple (map(int,input("Enter elements: ").split()))
#print(t)
#t= tuple (map(str,"123"))
#print(t)

t1=(1,2,3,4,5,4,5,34,34,2,45,35,234,54,5,325,45)
#print("Sum is :",sum(t1))
#print("Max is :",max(t1))
#print("Min is :",min(t1))
#print("Length is :",len(t1))
#t2 =(4,4,3,54,2,5,2,4)
#print(t1+t2)
#print(t1*3)

print(t1[1:5:2])
print(t1[:5])
print(t1[10:len(t1)])
print(t1[::])
print(t1[:])
print(t1[:-4])
'''
#Dictonary
''' A dictonary is a collection which is orderable and chageable index. In python Dictonary are Written with {}
and they have keya and values.
'''
'''
d  = {101:'Rohit',
      102:'Shivam',
      103:'Vikarma'}
print(d.get(101))
'''
#print(d)
#print(d[101])
#d[104]='Bital'
#print(d)
#del d[104]
#print(d)
#for i in d:
#    print(i,":",d[i])
d={}
for i in range(4):
    key = input("key: ")
    value = int(input("Value: "))
    d[key] = value

print(d)
    
    
