class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, product, price):
        self.items[product] = price
        print(self.items)

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]
        print(self.items)

    def get_price(self, product):
        if product in self.items:
            print(f"Цена на '{product}' - {self.items[product]}")
        else:
            print('None')

    def update_price(self, product, price):
        if product in self.items:
            self.items[product] = price
        print(self.items)


prostore = Store('Prostore', 'Minsk')
prostore.add_product('apples', 0.5)
prostore.add_product('bananas', 0.75)
prostore.add_product('blueberries', 0.65)
prostore.remove_product('blueberries')
prostore.get_price('bananas')
prostore.get_price('apples')
prostore.get_price('blueberries')
prostore.update_price('apples', 0.6)

gippo = Store('Gippo', 'Brest')
gippo.add_product('cherries', 0.7)
gippo.add_product('strawberries', 0.8)
gippo.add_product('cucumbers', 0.4)
gippo.remove_product('strawberries')
gippo.get_price('cherries')
gippo.get_price('cucumbers')
gippo.update_price('cucumbers', 0.35)

santa = Store('Santa', 'Grodno')
santa.add_product('tomatoes', 0.2)
santa.add_product('pineapples', 0.9)
santa.add_product('peaches', 0.8)
santa.remove_product('peaches')
santa.get_price('tomatoes')
santa.get_price('pineapples')
santa.update_price('tomatoes', 0.25)