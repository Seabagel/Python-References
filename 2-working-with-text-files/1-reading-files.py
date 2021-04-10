# Reading files into Python

# The open function creates a file object
#(a way of getting at the contents of the file),
# which is then stored in the variable f.
f = open("months.txt")
# f.read() tells the file object to read the full
# contents of the file, and return it as a string.
print(f.read())
print("\n")

k = open("months.txt")
# Reading by smaller pieces
next = k.read(1)
while next != "":
    print(next)
    next = k.read(1)
