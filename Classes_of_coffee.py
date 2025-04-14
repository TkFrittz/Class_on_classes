# Class on Classes.. With coffee

import sys

class coffee_class:
    def __init__(self,name,espresso,milk,foam,ice,hot):
        self.name = name
        self.espresso = espresso
        self.milk = milk
        self.foam = foam
        self.ice = ice
        self.hot = hot

    def explain_coffee(self):
        print("Ah yes the " + self.name + "..." )
        if self.espresso == True:
            print("It is a strong drink, made with espresso.")
        if self.milk == True:
            print("It is made with Milk.")
        if self.foam == True:
            print("It is made with Foam.")
        if self.ice == True:
            print("It is served cold.")
        if self.hot == True:
            print("It is served hot.")

hot_latte = coffee_class("Hot Latte",True,True,True,False,True)
iced_latte = coffee_class("Iced Latte",True,True,True,True,False)
drip_coffee_with_cream = coffee_class("Drip",False,True,False,False,True)
black_drip_coffee = coffee_class("Black Drip",False,False,False,False,True)


coffee_map = {
    "hotlatte": hot_latte,
    "icedlatte": iced_latte,
    "dripcoffee": drip_coffee_with_cream,
    "blackdripcoffee": black_drip_coffee,
}

print("Welcome to the Coffee Shop!")


def normalize_input(user_input):
    return user_input.lower().replace(" ", "")

def get_user_choice():
    print("Your options are: Hot Latte, Iced Latte, Drip Coffee, or Black Drip Coffee\n")
    attempts = 3
    while attempts > 0:
        user_input = input("Which drink would you like to know about? ").strip()
        normalized = normalize_input(user_input)
        if normalized in coffee_map:
            return coffee_map[normalized]
        else:
            attempts -= 1
            print(f"😬 Sorry, I didn't catch that. You have {attempts} tries left.\n")
    print("Too many failed attempts. Come back when you know your coffee. ☕")
    return None


# Run it Up bro!
selected_coffee = get_user_choice()

if selected_coffee:
    selected_coffee.explain_coffee()
    print("Thank you for shopping with Coffee Class!")
    print("Goodbye!")
    sys.exit()
