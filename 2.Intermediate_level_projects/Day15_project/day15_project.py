import day15_project_data as data
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

resources = data.resources
money = 0
def coin_converter():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies


def machine_report():
    for i in resources:
        if i == "coffee":
            unit = "g"
        else:
            unit = "ml"
        print(f"{i}: {resources[i]} {unit}".title())
    print(f"Money ${money}")


def ingredient_sufficiency(input):
    for ingredient in resources:
        if ingredient in ingredient_requirement:
            if input[ingredient] > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}")
                return False
            else:
                return True
                

def ingredient_calc():
    global resources
    for i in resources:
        if i in ingredient_requirement:
            resources[i] -= ingredient_requirement[i]


proceed = True
while proceed:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        machine_report()

    else:
        price = float(data.MENU[user_input]['cost'])
        ingredient_requirement = data.MENU[user_input]['ingredients']
        print("Please insert coins.")
        input_total = coin_converter()

        sufficient_ingredient = ingredient_sufficiency(ingredient_requirement)

        if input_total > price:
            if sufficient_ingredient == True:
                ingredient_calc()
                change = input_total - price
                money += price
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry, there are not enough resources. Money refunded")

        elif input_total < price: 
            if sufficient_ingredient == True:
                ingredient_calc()
                money += price
                print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Sorry, there are not enough resources. Money refunded.")

        elif input_total == price:
            if sufficient_ingredient == True:
                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry, there are not enough resources. Money refunded.")

        else:
            print("There isn't enough resources. Please refill.")
            proceed = False