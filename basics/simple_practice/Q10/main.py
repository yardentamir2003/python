import random
# import re


def main():
    names_dict = {}
    while True:
        option = input("1. Add new player\n2. Show balances\n3. Play\n4. Quit\nEnter your selection: ")
        # if valid_option(option):
        if option == "1" or option == "2" or option == "3" or option == "4":
            choose_option(option, names_dict)
        else:
            print("please enter 1/2/3/4.")

# def valid_option(option):
#     match = re.findall('^(?:1|2|3|4)$"', option)
#     if len(match) == 0:
#         return False
#     return True


def choose_option(option, names_dict):
    if option == "1":
        option_one(names_dict)
    if option == "2":
        option_two(names_dict)
    if option == "3":
        option_three(names_dict)
    if option == "4":
        exit(1)


def option_one(names_dict):
    player_name = input("Enter your name: ")
    random_cash = random.randint(0, 50)
    entry_cash_amount = 50 + random_cash
    print("Welcome {}, we randomized for your entry amount of {}$.".format(player_name, entry_cash_amount))
    names_dict[player_name] = entry_cash_amount


def option_two(names_dict):
    print("The balances are:")
    for key, value in names_dict.items():
        value = "{}$".format(value)
        print(key, value)


def option_three(names_dict):
    while True:
        name = input("Enter your name: ")
        if name in names_dict.keys():
            break
        else:
            print("Error. The name entered does not exist in the existing players.")

    while True:
        bet_money = int(input("How much money do you want to bet on? "))
        players_balance = names_dict[name]
        if bet_money <= players_balance:
            break
        else:
            print("Error. The amount of money is higher than the balance of the player")

    roll_dice(bet_money, name, names_dict)


def roll_dice(bet_money, name, names_dict):
    dice_result = random.randint(1, 6)
    print("Rolling the dice…… The dice shows {}.".format(dice_result))
    if dice_result == 1 or dice_result == 2 or dice_result == 3:
        print("You lost {}$".format(bet_money))
        names_dict[name] -= bet_money
    if dice_result == 4 or dice_result == 5:
        print("the bet is returned without any profit.")
    if dice_result == 6:
        bet_money = bet_money * 3
        print("You won {}$!".format(bet_money))
        names_dict[name] += bet_money


main()
