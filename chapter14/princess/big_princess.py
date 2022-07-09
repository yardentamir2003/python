from chapter13_classes.princesses.princess import Princess


class BigPrincess(Princess):
    def __init__(self, name):
        super().__init__(name)
        self.jump_count = 0

    def jump(self):
        self.jump_count = self.jump_count + 1
        for times in range(self.jump_count):
            print("up", end="")
        print()

