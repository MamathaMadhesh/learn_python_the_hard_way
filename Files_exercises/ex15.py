# Reading Files
from sys import argv

script,file_name=argv

txt=open(file_name)

print("Here is your file {}".format(file_name))
print(txt.read())

print(f"Type the filename again:")
file_again=input()

txt_again=open(file_again)

print(txt_again.read())