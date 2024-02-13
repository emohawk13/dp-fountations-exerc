from os import listdir
import os


print(listdir())

file_finder = os.listdir()

for filepath in file_finder:
    if os.path.isdir(filepath):
        print("/" + filepath)
    else:
        print(filepath)

# rewrite a file
with open("demo2.txt", "w") as myfile:
    myfile.write("I am starting this file from scratch.")
# append to a file
with open("demo2.txt", "a") as myfile:
    myfile.write("Check it out. I am writing!")

with open("demo2.txt", "r") as myfile:
    print(myfile.read())


# creating a new file
# my_file = open("a_new_file.txt", "x")
# my_file.close()
