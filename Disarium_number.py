number = int(input("Enter a number: "))

temp = number
digits = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = number
sum = 0
position = 1

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** position
    temp = temp // 10
    position = position + 1

if sum == number:
    print(number, "is a Disarium number")
else:
    print(number, "is not a Disarium number")