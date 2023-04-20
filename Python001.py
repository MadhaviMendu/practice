
# Write a program in Python to check given number is prime or not.


num = int(input("enter the number: "))
if num>1:
    for i in range(2,num/2):
        if(num % i==0):
           print(num,"the not number is Prime")
           break
        else :
           print(num,"the  number is Prime")  
    else :
        print(num, "the number is not prime")   

