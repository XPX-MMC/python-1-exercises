def calculator(): #Creating a function with NO parameters. because we are taking the input for the users
    number = int(input("Enter number 1: "))     #reading input from user and casting it as an int
    number_2 = int(input("Enter number 2: "))    #reading input from user and casting it as an int
    operation = str(input("Enter operation(+,*,/,-): "))   #Read operation from user

    if operation == "+":    #condtion #1 operation is '+'
        return number + number_2  #return sum of the two numbers
    elif operation == "-":
        return number - number_2
    elif operation == "*":
        return number * number_2
    elif operation == "/":
        return number / number_2
    else:
        return "Operation not valid. Try again" # return is not valid if sign is not an operation

while True:     #while true keep asking user for input to repeat the program
    result =  calculator()
    print(result)