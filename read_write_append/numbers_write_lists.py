# write_numbers_lists.py
# this program saves a list of numbers to a file
def main():
	# create a list of numbers
	numbers = [1,2,3,4,5]
	
	# open a file named zodiacAnimals.txt
	outfile = open("numbersLists.txt", "w")
	
	# write the numbers to the file
	for item in numbers:
		outfile.write(str(item) + "\n")
	
	# close the file
	outfile.close()
	
	print("Data writen to numbersLists.txt")

# call the main function
main()