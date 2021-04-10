foods = {}
foods["banana"] = "A delicious and tasty treat!"
foods["dirt"] = "Not delicious. DO NOT EAT!"
print(foods["banana"])
del foods["dirt"]

if "cheese" in foods:
  print("Cheese is one of the known foods!")
  print(foods["cheese"])
  
ingredients = {}
ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]
print(ingredients)

europe = []
germany = {"name": "Germany", "population": 81000000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000}
europe.append(luxembourg)
for countries in europe:
  print(countries)
