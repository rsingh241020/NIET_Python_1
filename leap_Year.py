Year =int(input("Enter Your 4 Digit Year :"))

if(Year%4 ==0 and Year%100 !=0) or (Year%400==0):
    print("Year is a leap Year",Year)
else:
    print("Year is a Not Leap Year",Year)
