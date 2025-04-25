class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item, quantity=1):
        if self.items.get(item, 0) < quantity:
            raise ValueError(f'Not enough {item}')
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]

    def has_item(self, item, quantity=1):
        return self.items.get(item, 0) >= quantity

    def get_items(self):
        return dict(self.items)
