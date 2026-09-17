class chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Si[[ing Chai")

    def add_sugar(self, amount):
        print("Added the sugar")

my_chai = chai(sweetness=5, milk_level=3)
my_chai.add_suggar(3)