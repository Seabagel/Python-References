# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # clean up the person's name
    name = name.strip().capitalize().replace("  "," ")
    # check if this person already voted
    if name in voted:
        print(name + " has already voted! Fraud!")
        continue
    voted.append(name)
    # munge the vote string to clean it up
    vote = vote.strip().capitalize().replace("  "," ")
    if not vote in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] += 1

print("Results:")
print()
for name in counts:
    print(name + ": " + str(counts[name]))
