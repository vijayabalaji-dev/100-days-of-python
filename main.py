from data import resources, MENU

machine_amt = 0


def check_resource(coffee_type):
    if coffee_type == "espresso":
        if resources['water'] > 50 and resources['coffee'] > 18:
            return True
        else:
            return False
    if coffee_type == "cappuccino":
        if resources['water'] > 250 and resources['coffee'] > 24 and resources['milk'] > 100:
            return True
        else:
            return False
    if coffee_type == "latte":
        if resources['water'] > 200 and resources['coffee'] > 24 and resources['milk'] > 150:
            return True
        else:
            return False


def calculate_total(coffee_type, quarters_amt, dimes_amt, nickles_amt, pennies_amt):
    total_amt = round((quarters_amt * 0.25) + (dimes_amt * 0.1) + (nickles_amt * 0.05) + (pennies_amt * 0.01), 2)
    coffee = check_resource(coffee_type)
    if coffee:
        if total_amt < MENU[user_input]['cost']:
            print("not enough money")
            print(f"here is your amount {total_amt}")
        else:
            change = round(total_amt - MENU[user_input]['cost'], 2)
            if change > 0:
                print(f"Here is your change {change}")
            return True
    else:
        print("not enough resources")
        print(f"here is your amount {total_amt}")
        return False


varieties = ["espresso", "latte", "cappuccino"]
exit_loop = False
while not exit_loop:
    user_input = input("What would you like? (espresso/latte/cappuccino):").strip()

    if user_input not in varieties:
        if user_input == "report":
            print(f"water : {resources['water']}")
            print(f"milk : {resources['milk']}")
            print(f"coffee : {resources['coffee']}")
            print(f"amount in machine : {machine_amt}")
        elif user_input == "off":
            exit_loop = True
        else:
            print("Choose from the given list")
            exit_loop = True

    else:
        print("Please insert coins ")
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))

        amt = calculate_total(user_input, quarters, dimes, nickles, pennies)
        if amt:
            machine_amt += MENU[user_input]['cost']
            resources['water'] -= MENU[user_input]['ingredients']['water']
            resources['coffee'] -= MENU[user_input]['ingredients']['coffee']
            if user_input != 'espresso':
                resources['milk'] -= MENU[user_input]['ingredients']['milk']
            print("here is your coffee 😘😁")
        else:
            exit_loop = True
            print("not enough resources 🥲")
