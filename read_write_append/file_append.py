# file_append.py
# this program opens animals.txt file and appends additional animals
def main():
	# open a file named animals.txt
	outfile = open("animals.txt", "a")
	
	# append three animals to the file
	outfile.write("Rabbot\n")
	outfile.write("Dragon\n")
	outfile.write("Snake\n")
	
	# close the file
	outfile.close()
	
	print("operation complete.")

# call the main function
main()