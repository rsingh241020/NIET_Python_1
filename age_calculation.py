#input a Age 0-12=child 13-19=te an age 20-60=adult 60<senoior cidtrdfgndfklg

age=int(input("Enter Your Age"))

if(age<=13):
    print("You are a Child")
elif(age>13 and age<=19):
    print("You are a Teen Age")
elif(age>19 and age<=60):
    print("You are a Adult")
else:
    print("Your Are a Senior citizen")
