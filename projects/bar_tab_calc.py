# WORK IN PROGRESS

class Tab:
    
    menu = {
        'wine': 5,
        'beer': 3,
        'soft_drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'dessert': 6
    }
    def __init__(self):
        self.total = 0
        self.items = []
    
    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]
    
    def print_bill(self, tax, gratuity):
        tax = (tax/100) * self.total
        gratuity = (gratuity/100) * self.total
        total = self.total + tax + gratuity
        for item in self.items:
            print(f'{item:15} ${self.menu[item]}')        
        print(f'{"Total":15} ${total:.2f}')