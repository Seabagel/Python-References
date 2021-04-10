for line in open("radishsurvey.txt"):
    # line was "Jin Li - White Icicle\n"
    line = line.strip()
    # Do something with each line
    
    #print(line)
    # After this line runs, parts has the value ['Jin Li', 'White Icicle']
    # "1,2,3,4,5".split(",") = [1,2,3,4,5]
    # "cheese".split(",") = ['c','h','e','e','s','e']
    parts = line.split(" - ") 
    name = parts[0]
    vote = parts[1]
    print(name + " voted for " + vote)
