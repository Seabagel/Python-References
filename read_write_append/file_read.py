# file_read.py
# this program reads and displays the contents of animals.txt file
def main():
	# open a file named animals.txt
	infile = open("animals.txt", "r")
	
	# read three lines from the file
	line1 = infile.readline()
	line2 = infile.readline()
	line3 = infile.readline()
	
	# close the file
	infile.close()
	
	# print the data that was read into the memory
	print(line1)
	print(line2)
	print(line3)

# call the main function
main()