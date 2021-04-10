# read_numbers_lists.py
# this program reads a file's contents into a list
def main():
	# open a file for reading
	infile = open("numbersLists.txt", "r")
	
	# read from the file
	numbers = infile.readline()
	
	# close the file
	infile.close()
	
	# print the contents of the lst
	print(numbers)
	
	for index in range(len(numbers)):
		numbers[index] = numbers[index].rstrip("\n")
		print(numbers[index])
		
# call the main function
main()