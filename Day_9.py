'''d1 = {}
for i in range(3):
    key = input("key: ")
    value = int(input("value: "))
    d1[key] = value
print(d1) 
'''
'''
d = {101:'Rohit',
     102:'Vishal',
     103:'Rajnish'}
#print(d)
#d1={}

#d.update({104:'Dr',105:'Harsh'})
#d1 = d.copy()
print(d)
d.pop(102)
print(d)
#d.clear()
#print(d)
print(d.keys())
print(d.values())
'''

'''
set1 = {1,2,1,2,3,4,2,3,2,21,1,2}
print(set1)
print(type(set1))

set2 =set([1,2,"rohit",2,3,4,4,3])
print(set2)
s3 = set([1,2,3,4,3,2,2,2,1,1])

print(s3)
    #s3=([1,4,5,6,"rohit",322,3,2,2,22,65.5,54,67.78,5,2])
#print(s3)
'''
s1 =set([1,2,'Rohit',4,2])
#for i in s1:
#    print(i)
#print('Rohit' in s1,)
#s1.remove(4)
#s1.add("Raamu")
#print(s1)

# update method updates the set with different element
s2 =set([1,2,3,3,4,5,4334,3,5,])
s1.update(s2)
#print(s1)
'''
#remove
s1.remove(2)
print(s1)
#copy
s = s1.copy()
print(s)
#clear
s.clear()
print(s)
'''
#s3={1,2,3,4,3.4,50,3.4}

#
#Discard -Discard remove an element is it is an member
'''s4= set([1,2,3,4,5])
s4.discard(2)
print(s4)
'''
a = {23,2,3,54}
b = {2,3,6,5}

#print(a.union(b))
#print(a|b)
'''
print(a.intersection(b))
print(a&b)
print(a-b)
print(a.difference(b))
print(a.symmetric_difference(b))
print(a^b)#symmetric

print(a.isdisjoint(b))
'''


print(a.issubset(b))
print(a.issuperset(b))
