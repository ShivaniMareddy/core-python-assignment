def calculate_total(cart_items):
    if cart_items==0:
        return "Cart is empty!"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9 
    return total
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
result = calculate_total(cart_items)
print(f"Total Price: {result}")
