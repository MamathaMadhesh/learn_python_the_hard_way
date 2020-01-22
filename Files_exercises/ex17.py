# Copy one file to another file

from sys import argv
from os.path import exists

script,file1,file2=argv

print(f" copying from {file1} to {file2}")

in_file=open(file1)
indata=in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the file exists? {exists(file2)}")

print(f"If you don't want hit CTRL-C(^C).")
print("If you do want that hit RETURN.")

input("?")

oufile=open(file2,'w')
oufile.write(indata)

print("All right all done")
oufile.close()
in_file.close()