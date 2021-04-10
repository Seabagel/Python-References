f = open("months.txt")
#print(f.readlines())
##for month in f.readlines():
##   print("Month " + month.strip())
for month in f:
   print("Month " + month.strip())
