print('Calculator Functions')

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


print('Addition function')

def addition(num1,num2):
    return num1+num2


print('Multiplication function')

def multiplication(num1,num2):
    return num1*num2


print("1. Addition")
print("2. Multiplication")

choice = int(input("Enter your choice: "))


if choice == 1:
    print("The sum of the two numbers is",addition(num1,num2))

elif choice == 2:
    print("The product of the two numbers is",multiplication(num1,num2))