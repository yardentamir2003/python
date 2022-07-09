class Princess:
    # constructor
    def __init__(self, name):
        self.name = name
        self.count = 0

    def hello(self):
        self.count = self.count + 1
        print("I am princess {}, {} times".format(self.name, self.count))
