import csv

class Item:
    all = []
    
    def __init__(self, category, name, price, quantity = 0):
        self.category = category
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Item.all.append(self)
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                category =item.get('Category'),
                name=item.get('Name'),
                price=float(item.get('Price')),
                quantity=int(item.get('Quantity'))
            )
    
    def __repr__(self):
        # use self.__class__.__name__ to access name of child class used to create instance
        return f"{self.__class__.__name__}('{self.category}', '{self.name}', {self.price}, {self.quantity})"
    
    def list_items(self):
        foods = Item.all
        for food in foods:
            print(f"Category: {food.category}, Name : {food.name}, Price: ${food.price}, Quantity: {food.quantity}")


Item.instantiate_from_csv()
print(Item.all)
Item.list_items(Item)