#print("Counting votes for White Icicle...")
#count = 0
#for line in open("radishsurvey.txt"):
#   line = line.strip()
#   name, vote = line.split(" - ")
#   if vote == "White Icicle":
#      count = count + 1
#print(count)

def count_votes(radish):
    print("Counting votes for " + radish + "...")
    count = 0
    for line in open("radishsurvey.txt"):
        line = line.strip()
        name, vote = line.split(" - ")
        if vote == radish:
            count = count + 1
    return count

print(count_votes("White Icicle"))

print(count_votes("Daikon"))

print(count_votes("Sicily Giant"))
