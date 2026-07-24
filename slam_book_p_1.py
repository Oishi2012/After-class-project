# importing the module
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

    return int(input("Enter Choice"))


print("Welcome to the Slambook Application")

sb = initial_slambook()

while True:
    ch = menu()

    if ch == 5:
        print("Good Bye!")
        break