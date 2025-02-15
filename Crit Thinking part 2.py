#Program to multiply and divide two numbers

#Announce that the program only works with numbers
print("IMPORTANT: Please enter only numbers")

#in case the user enters a non integer or inputs num2 as zero
while True:
    try:
        #values
        num1=int(input('Enter the first number you want to multiply and divide = '))
        num2=int(input('Enter the second number you want to multiply and divide = '))
        if num2 == 0:
            print("Error, you can not divide by zero, please change the second number so it is not zero")
        else:
            break
    except ValueError:
        print("Please enter a valid integer")

#operations
multiplication = num1 * num2
division = num1 / num2    

#output
print('The result of your multiplication is =', multiplication)
print('The result of your division is =', division)

#so the program doesn't close as soon as the answer is given
input("Press enter to close the program")
