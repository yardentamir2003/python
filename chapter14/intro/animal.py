class Animal:
    def __init__(self, animal_name):
        self.name = animal_name
        self.count = 0

    def say_name(self):
        self.count += 1
        print("my name is {} and i said it {} times".format(self.name, self.count))
