import random


def main():
    menu = []
    create_line_list("side_dishes", menu)
    create_line_list("main_dishes", menu)
    create_line_list("desserts", menu)
    side_dish = menu[0]
    main_dish = menu[1]
    dessert = menu[2]
    print("today's menu is {}, {}, and {}. \nBon Apatite!".format(side_dish, main_dish, dessert))


def create_line_list(file_name, menu):
    with open(file_name, "r") as file:
        line_list = []
        for line in file:
            line = line.rstrip()
            line_list.append(line)
    choose_random_item(line_list, menu)


def choose_random_item(line_list, menu):
    dish = random.choice(line_list)
    menu.append(dish)


main()
