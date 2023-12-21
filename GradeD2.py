Eng=int(input("enter English sub Number "))
Hin=int(input("enter Hindi sub Number "))
Mat=int(input("enter Math sub Number "))
Sci=int(input("enter Science sub Number "))
Sst=int(input("enter Social science sub Number "))
Total = Eng+Hin+Mat+Sci+Sst

per =(Total/500)*100
print("Total Marks: ",Total)
print("Total Percentage :",per)
if(per <=40):
        print("E")
elif(per>40 and per <=60):
    print("D")
elif(per>60 and per <=70):
    print("C")
elif(per>70 and per<=90):
    print("B")
else:
    print("A")
