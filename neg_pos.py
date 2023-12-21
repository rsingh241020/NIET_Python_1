print("-------------------------CalCulator---------------------------------")


num1=float(input("Enter first Number"))
num2=float(input("Enter Second Number"))


print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Divison")
sym = int(input("What Do You Want To Do : \n "))
if(sym ==1):
    print("Addition is ",num1+num2)
if(sym ==2):
    print("Substraction is ",num1-num2)
if(sym ==3):
    print("Multiplication is ",num1*num2)
if(sym ==4):
    print("Division is ",num1/num2)
