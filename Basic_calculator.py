def get_numbers():

    numbers = []

    while True:

        number = input("Enter a number or type 'done' to stop: ")

        if number == "done":

            break

        numbers.append(float(number))

    return numbers


def sum_numbers():

    numbers = get_numbers()

    result = sum(numbers)

    total_inputs = len(numbers)

    return result, total_inputs


def difference_numbers():

    numbers = get_numbers()

    result = numbers[0]

    for number in numbers[1:]:

        result = result - number

    total_inputs = len(numbers)

    return result, total_inputs


def product_numbers():

    numbers = get_numbers()

    result = 1

    for number in numbers:

        result = result * number

    total_inputs = len(numbers)

    return result, total_inputs


def average_numbers():

    numbers = get_numbers()

    result = sum(numbers) / len(numbers)

    total_inputs = len(numbers)

    return result, total_inputs


def main():

    print("Basic Calculator")

    print("1. Sum")

    print("2. Difference")

    print("3. Product")

    print("4. Average")


    choice = input("Enter your choice: ")


    if choice == "1":

        result, total_inputs = sum_numbers()


    elif choice == "2":

        result, total_inputs = difference_numbers()


    elif choice == "3":

        result, total_inputs = product_numbers()


    elif choice == "4":

        result, total_inputs = average_numbers()


    else:

        print("Invalid choice")

        return


    print("Final Answer:", result)

    print("Total Input Numbers:", total_inputs)


main()