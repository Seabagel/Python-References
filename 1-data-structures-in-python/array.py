#Arrays
shopping_list = []

shopping_list.append("milk")
shopping_list.append("cheese")
shopping_list.append("bread")
print(shopping_list)

shopping_list.remove("milk")
for things in shopping_list:
  print(things)
  
shopping_list.append("milk")
if "milk" in shopping_list:
  print("Delicious!")
if "eggs" not in shopping_list:
  print("We need eggs")
  shopping_list.append("eggs")
print("\n")