name = "Fatema"
age = 14
grade = 7
height = 5.1

print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("Grade :", grade)
print("Data Type of Grade is", type(grade))

print("Height :", height)
print("Data Type of Height is", type(height))


print("\nAfter Type Casting....")

age = str(age)
grade = str(grade)
height = str(height)

print(age)
print("Data Type of age is", type(age))

print(grade)
print("Data Type of grade is", type(grade))

print(height)
print("Data Type of height is", type(height))


sentence1 = "My name is " + name + "."
sentence2 = "I am " + age + " years old."
sentence3 = "I study in grade " + grade + "."
sentence4 = "I am " + height + " feet tall."

print("\nFirst Sentence :", sentence1)
print("Second Sentence :", sentence2)
print("Third Sentence :", sentence3)
print("Fourth Sentence :", sentence4)


full_sentence = sentence1 + " " + sentence2 + " " + sentence3 + " " + sentence4

print("\nAfter Concatenation....")
print("Full Sentence :", full_sentence)