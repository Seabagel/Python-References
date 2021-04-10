for line in open("radishsurvey.txt"):
   line = line.strip()
   parts = line.split(" - ")
   # This code assigns each variable to the corresponding item in 'parts'.
   name, vote = parts
   #name, cheese, cracker = "Fred,Jarlsberg,Rye".split(",")
   if vote == "White Icicle":
      print(name + " likes White Icicle!")
