
from day16_project_menu import Menu, MenuItem
from day16_project_coffee_maker import CoffeeMaker
from day16_project_money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


menu = Menu()
options = menu.get_items()

proceed = True

while proceed:
    user_input = input(f"What would you like? Options are: {options}.")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()

    elif user_input == "off":
        proceed = False

    else:
        drink = menu.find_drink(user_input)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources == True:
            payment_accepted = money_machine.make_payment(drink.cost)
            if payment_accepted == True:
                coffee_maker.make_coffee(drink)
            else:
                print("The money is insufficient. Money refunded.")
        else:
            print("The resources is insufficient. Money refunded.")