f = open("months.txt")
next = f.readline()
while next != "":
    #print(next)
    print(next.strip())
    next = f.readline()
    ##next = next.strip()
    ##print(next)
    
