# File handling in Python
# Opening a file
with open('coding.txt','w') as file:
    file.write('Hi! I am Penguin. ')

#split file into words
with open('coding.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)



# Checking if a file exists or not
import os

print('Checking if file exists or not')
if os.path.exists('My_file.txt'):
    print('My_file.txt exists')
else:
    print('My_file.txt does not exist')
    with open("My_file.txt", "w") as file: 
     file.write("Hello, I am Fatema. I love coding!")

#removing files

print('Checking if file exists or not')
if os.path.exists('sample_doc.txt'):
    os.remove('sample_doc.txt')
    print('File removed successfully')
else:    print('It does not exist')
