a = int(input("Enter the Value of a :"))
b = int(input("Enter the Value of b :"))
c = int(input("Enter the Value of c :"))
D=(b*b)-(4*a*c)
deno=2*a
if(D>0):
    print("Real Number ")
    root1= (-b + D**0.5)/demo
    root2= (-b - D**0.5)/demo
    print("Root1 : =",root1,"\tRoot2 =",root2)
elif(D==0):
    print("Equal Roots")
    root1=-b/deno
    print("Root1 and Root2 = ",root1)
else:
    print("Imaginary Root")
