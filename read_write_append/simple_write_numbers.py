# write_numbers.py
# this program demonstrates how numbers must be converted to strings
# before they are written to a text file
def main():
	# open a file named animals.txt
	outfile = open("simpleNumbers.txt", "w")
	
	# get three numbers from the user
	num1 = int(input("enter a number: "))
	num2 = int(input("enter a number: "))
	num3 = int(input("enter a number: "))
	
	# write the numbers to the file
	outfile.write(str(num1) + "\n")
	outfile.write(str(num2) + "\n")
	outfile.write(str(num3) + "\n")
	
	# close the file
	outfile.close()
	
	print("Data writen to simpleNumbers.txt")

# call the main function
main()