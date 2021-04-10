# In Python, you don't have to close a statement. Instead of using "{}", you only need to put colons ":"
# when you begin a function or if statement. 
# You can print value of a function

def greater_less_equal_5(answer):
    if answer > 5:
        print("More than")
    elif answer < 5:          
        print("Less than")
    else:
        print("Equal to")

greater_less_equal_5(4)
greater_less_equal_5(5)
greater_less_equal_5(6)

# You can return value of a function
def greater_5(answer):
    if answer > 5:
        return True
    else:
        return False

greater_5(4)
greater_5(5)

# You can combine if statement with function
def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'. \n").lower()
    
    if answer == "left":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()
		
clinic()