# funtion to add numbers
def add(x, y):
    return x + y

# function for subtraction 
def subtract(x, y):
    return x - y

# function for multiplication 
def multiply(x, y):
    return x * y

# function for divide
def divide(x, y):
    return x / y


def calculate(operation):   
    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        if operation == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
    

while True:
    # take input from the user
    operation = input("Please choose operation : ")
    if operation in ('+', '-', '*', '/'):
        calculate(operation) 
        nextCalculation = input("Let's have some more fun, choose yes for next calculation, choose bulk for bulk calcualation, choose no for terminate.  (yes/bulk/no): ")
        if nextCalculation == "no":
            break
        elif nextCalculation == "bulk":
            fileName = input("Please enter the file name as input.txt : ")
            if fileName == "input.txt":
                try: 
                    file = open(fileName, 'r')
                    print(file.read())
                    file.close()
                    break
                except FileNotFoundError as error :
                    print("The file that you are trying to open does not exist")
                    print(error)
                    break
    else :
        print("Invalid operation")                
