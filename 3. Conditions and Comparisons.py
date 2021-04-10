# Comparation Operators
# ------------------------
3 < 4
5 >= 5
10 == 10
12 != 13

# Boolean Operators
# ------------------------
True or False 
(3 < 4) and (5 >= 5)
this() and not that()

The boolean operator and returns True when the expressions on both sides of and are true. 
The boolean operator or returns True when at least one expression on either side of or is true.
The boolean operator not returns True for false statements and False for true statements.

not is evaluated first;
and is evaluated next;
or is evaluated last.

True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

# Conditional statements
# ------------------------
if this_might_be_true():
    print "This really is true."
elif that_might_be_true():
    print "That is true."
else:
    print "None of the above."
