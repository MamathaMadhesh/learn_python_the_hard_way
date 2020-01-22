# Reading and writing Files
from sys import argv

script,file_name=argv

print(f"we are going to erase {file_name}")
print(f"If you don't want hit CTRL-C(^C).")
print("If you do want that hit RETURN.")

input("?")
print("Opening the file..")
target=open(file_name,'w+')


print("Now I'm truncating the file")
target.truncate()

print("Now I'm going to ask for three lines")
line1=input("Line1: ")
line2=input("Line2: ")
line3=input("Line3: ")

print("Im going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally. we close it.")
target.close()

# Reading the file 

print(f"Type the filename again:")
file_again=input()

txt_again=open(file_again)

print(txt_again.read())