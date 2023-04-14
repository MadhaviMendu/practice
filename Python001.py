
# Write a program in Python to check whether an integer is Armstrong number or not.
# Write a program in Python to check given number is prime or not.
# Write a program in Python to find greatest among three integers.

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

