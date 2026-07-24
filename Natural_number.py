number = int(input("Enter Number to Check"))

print("Number to be checked :", number)

if number > 0:
    print("This is a positive number")
    print("This is a natural number")

elif number < 0:
    print("This is a negative number")
    print("This is not a natural number")

else:
    print("This is neutral")
    print("This is not a natural number")


print("\nChecking the Number Again....")

if number % 2 == 0:
    print("This is an even number")

else:
    print("This is an odd number")


numbers = [number]

print("\nNumber List :", numbers)
print("Length of list:", len(numbers))
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

numbers.append(1)
print("Updated List :", numbers)

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List :", numbers)

print("Multiplication on List :", numbers * 2)

numbers = numbers[:2]
print("Sliced List :", numbers)

numbers.clear()
print("Updated List :", numbers)