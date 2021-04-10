# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    # munge the vote string to clean it up
    vote = vote.strip().capitalize()
    # The replace function can replaces all double spaces with a single space:
    vote = vote.replace("  ", " ")
    if vote not in counts:
        # First vote for this variety
        counts[vote] = 1
    else:
        # Increment the vote count
        counts[vote] = counts[vote] + 1
        
#print(counts)
for name in counts:
    count = counts[name]
    print(name + ": " + str(count))

