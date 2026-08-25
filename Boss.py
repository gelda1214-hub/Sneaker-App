class SneakerStore:
    def __init__(self):
        self.sneakers = []

    def add(self, sneaker):
        self.sneakers.append(sneaker)

    def show_sneakers(self):
        for sneaker in self.sneakers:
            print(sneaker.name, "-", "$", sneaker.price)


