# read_list.py
# this program reads a file's contents into a list
def main():
    # open a file named animals.txt
    infile = open("zodiacAnimals.txt", "r")

    # read three lines from the file
    animals = infile.readline()

    # close the file
    infile.close()

    # print the data that was read into the memory
    print(animals)

    for index in range(len(animals):
        animals[index] = animals[index].rstrip("\n")
        print(animals[index])

# call the main function
main()
