name = 'marcog'
number = 42
print('My name is ' + name + ' and my age is: ' + str(number))
print("My name is %s and my age is: %d" % (name, number))
print("My name is {} and my age is: {}".format(name, number))
print('My name is', name,'and my age is:', number)

# Output:
# My name is marcog and my name is 42

# "%.2f" % area
# "{0:.2f}".format(a)
# "{0}.2f".format(a)
# format(area,".2f")
