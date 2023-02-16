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

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        break
    elif coffee == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
        print(f"Money: ${profit}")
    else:
        make_coffee = True
        not_enough = []
        for item in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][item] > resources[item]:
                not_enough.append(item)
                make_coffee = False
                break
        
        if make_coffee == False:
            print(f"Sorry there is not enough {not_enough[0]}")
        else:   
            print("Please insert coins.")
            q = int(input("how many quarters?: "))
            d = int(input("how many dimes?: "))
            n = int(input("how many nickles?: "))
            p = int(input("how many pennies?: "))
            total = 0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p
            
            change = total - MENU[coffee]["cost"]

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += MENU[coffee]["cost"]
                for item in MENU[coffee]["ingredients"]:
                    resources[item] -= MENU[coffee]["ingredients"][item]
                print(f"Here is ${round(change, 3)} in change.")

                print(f"Here is {coffee} ☕. Enjoy!")
