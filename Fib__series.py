num1 = 0
num2 = 1
next_number = num1  
 
for i in range (10):
    print(next_number, end=" ")
    num1, num2 = num2, next_number   
    next_number = num1 + num2
    # 0 1 1 2 
