# file_write.py
# this program writes three lines of data to a file
def main():
	# open a file named animals.txt
	outfile = open("animals.txt", "w")
	
	# write the names of three animals to the file
	outfile.write("Rat\n")
	outfile.write("Ox\n")
	outfile.write("Tiger\n")
	
	# close the file
	outfile.close()
	
	print("operation complete.")

# call the main function
main()