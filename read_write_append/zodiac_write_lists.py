# write_lists.py
# this program saves a list of string elements to a file
def main():
	# create a list of strings
	animalOfZodiac = ["Rat","Ox","Tiger","Ravvit","Dragon","Snake","Horse","Sjeep","Monkey","Rooster","Dog","Pig"]
	
	# open a file named zodiacAnimals.txt
	outfile = open("zodiacAnimals.txt", "w")
	
	# write the numbers to the file
	for item in animalsOfZodiac:
		outfile.write(item + "\n")
	
	# close the file
	outfile.close()
	
	print("Data writen to zodiacAnimals.txt")

# call the main function
main()