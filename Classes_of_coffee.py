# Class on Classes.. With coffee
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
    "Hot Latte": hot_latte,
    "Iced Latte": iced_latte,
    "Drip Coffee": drip_coffee_with_cream,
    "Black Drip Coffee": black_drip_coffee,
}

coffee_of_choice = input("Hello, What drink would you like to know about? Your options are: Hot Latte, Iced Latte, Drip Coffee, or Black Drip Coffee \n ").strip().lower().title()

if coffee_of_choice in coffee_map:
    coffee_map[coffee_of_choice].explain_coffee()
else:
    print("Sorry I don't Understand. Leave my coffee shop you heathen!")