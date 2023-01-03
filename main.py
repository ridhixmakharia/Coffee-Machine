
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient_order(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print("Sorry there is not enough "+item)
            return False
    return True


def calculate_coins():
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def sufficient_money(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name} ☕️. Enjoy!")



on_off = "on"
while on_off != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        on_off = "off"

    elif user_input == "report":
        for key, value in resources.items():
            print(key + ": " + str(value) + "ml")
        print(f"Profit: ${profit}")
    else:
        flag = 0
        drink = MENU[user_input]
        if sufficient_order(drink["ingredients"]):
            payment = calculate_coins()
            if sufficient_money(payment, drink["cost"]):
                make_drink(user_input, drink["ingredients"])
