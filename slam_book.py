import sys

def initial_slambook():
    rows, cols = int(input("Please enter number of yours: ")), 5

    slam_book = []
    print(slam_book)

    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY): " % (i + 1))
        print("NOTE: * indicates mandatory fields")
        print("………………………………………………………………………………")

        temp = []

        for j in range(cols):

            if j == 0:
                temp.append(str(input("Enter name*: ")))

                if temp[j] == '' or temp[j] == ' ':
                    sys.exit(
                        "Name is a mandatory field. Process exiting due to blank field..."
                    )

            if j == 1:
                temp.append(int(input("Enter number*: ")))

            if j == 2:
                temp.append(str(input("Enter something about your friend: ")))

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(
                    str(input("Enter category(Family/Friends/Work/Others): "))
                )

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)

    print(slam_book)
    return slam_book


def menu():
    print("**********************************************************************")
    print("1. ADD")
    print("2. REMOVE")
    print("3. DELETE ALL")
    print("4. DISPLAY ALL")
    print("5. EXIT")

    return int(input("Enter Choice"))


def add_contact(pb):
    dip = []

    for i in range(len(pb[0])):

        if i == 0:
            dip.append(str(input("Enter name: ")))

        if i == 1:
            dip.append(int(input("Enter number: ")))

        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))

        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))

        if i == 4:
            dip.append(str(input("Enter category (Family/Friends/work/Others): ")))

    pb.append(dip)

    return pb


def thanks():
    print("******************************************************")
    print("Thank you for using our Slam Book.")
    print("Please visit again!")
    print("******************************************************")

    sys.exit("Goodbye, have a nice day ahead!")


print("........................................................")
print("Hello dear Friends, welcome to our Slam Book")
print("You may now proceed to explore this Slam Book and fill your details about your friends")

print("\t\tSMARTPHONE DIRECTORY", flush=False)

print("\tYou can now perform the following operation on this\nslambook\n")
print("1. Add a new contact")
print("6. Exit phonebook")

ch = 1

pb = initial_slambook()

while ch in (1, 2, 3, 4, 5):

    ch = menu()

    if ch == 1:
        pb = add_contact(pb)

    else:
        thanks()