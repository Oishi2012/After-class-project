# 1. Open the file and print the contents
with open("f1.txt", "r") as file:
    all_content = file.read()
    print(all_content)

# 2. Print the first ten characters
with open("f1.txt", "r") as file:
    first_ten_characters = file.read(10)
    print(first_ten_characters)

# 3. Print the first line
with open("f1.txt", "r") as file:
    first_line = file.readline()
    print(first_line)

# 4. Print the first four lines
with open("f1.txt", "r") as file:
    four_lines = file.readlines()[:4]
    print(four_lines)

# 5. Loop through the file and print lines one by one
with open("f1.txt", "r") as file:
    for line in file:
        print(line)


