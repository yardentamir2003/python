import random


def main():
    option = input("1. Add new player\n2. Show balances\n3. Play\n4. Quit\nEnter your selection: ")
    names_dict = {}
    choose_option()


def choose_option(option):
    if option == "1":
        option_one()
    # if option == "2":
    #     option_two()
    # if option == "3":
    #     option_three()
    # if option == "4":
    #     option_four()


def option_one(names_dict):
    player_name = input("Enter your name: ")
    random_cash = random.randint(0, 50)
    entry_cash_amount = 50 + random_cash
    print("Welcome {}, we randomized for your entry amount of {}$.".format(player_name, entry_cash_amount))
