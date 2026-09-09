class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for name, price in self.items)

    def avg(self):
        return sum(price for name,price in self.items) /  len(self.items)