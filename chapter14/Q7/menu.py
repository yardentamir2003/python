# import re


class Menu:
    def __init__(self):
        self.options = []

    def add_option(self, option_name, callback_function):
        option_function = (option_name, callback_function)
        self.options.append(option_function)

    def show_menu(self):
        while True:
            index = 1
            for option in self.options:
                print("{}. {}".format(index, option[0]))
                index += 1
            print("{}. quit".format(index))
            while True:
                chosen_option = input("Select option: ")
                if not chosen_option.isnumeric():
                    print("Please enter a numeric input.")
                    continue
                chosen_option_index = int(chosen_option)
                if chosen_option_index > index:
                    print("please select a number between 1-{}".format(str(index)))
                    continue
                if chosen_option_index == index:
                    return
                chosen_function = self.options[chosen_option_index - 1][1]
                chosen_function()
                break

#
# def foo():
#     print("1")
#
#
# def foo2():
#     print("2")
#
#
# def valid_option(option):
#     match = re.findall("^[123]$", option)
#     if len(match) == 0:
#         return False
#     return True
#
#
# if __name__ == '__main__':
#     menu = Menu()
#     menu.add_option("foo", foo)
#     menu.add_option("yarden", foo2)
#     menu.show_menu()
