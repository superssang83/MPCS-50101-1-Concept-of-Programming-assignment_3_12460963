# module-3-debugging.py
#
# Find all the errors in this program and correct them. The program should be 
# error free and run without any issues.

menu = {"burger": 5.00, "fries": 2.00, "cheeseburger": 6.00, "nuggets": 4.00, "ice_cream": 3.00}

def is_on_menu(choice):
    """Determines if the choice option is on the menu by comparing the price. 
    If option costs more then $0.00, return `True`, otherwise return `False`
    """

    if choice in menu and menu[choice] > 0.00:
        return True 
    else:
        return False

# returns the cost of choice 
def cost(choice):
    
    price = menu[choice]
    
    return price
# Ask the user what they would like to order
choice = input("What would you like to order? Our menues are 'burger', 'fries', 'cheeseburger', 'nuggets', 'ice_cream': ")

while not is_on_menu(choice):   
    print("We don't serve that. Please try again.")
    choice = input("What would you like to order? Our menues are 'burger', 'fries', 'cheeseburger', 'nuggets', 'ice_cream': ")
    
print("Your choice is:", choice)
print("That will be: $", cost(choice))