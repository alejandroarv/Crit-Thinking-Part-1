#Program to add and subtract two numbers

#Announce that the program only works with numbers
print("IMPORTANT: Please enter only numbers")

#In case the user enters a non integer
while True:
    try:
        #values
        num1=int(input('Enter the first number you want to add and subtract = '))
        num2=int(input('Enter the second number you want to add and subtract = '))
        break
    except ValueError:
        print("Please enter a valid integer")
        
#Operations
add = num1 + num2
subtract = num1 - num2

#Output
print('The result of your addition is =', add)
print('The result of your subtraction is =', subtract)

#So the program doesn't close as soon as the answer is given
input("Press enter to close the program")
