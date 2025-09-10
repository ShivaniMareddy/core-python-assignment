# Program: Restaurant Menu Management

def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu!")
def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(initial_menu, "Tacos")
remove_item(initial_menu, "Salad")
print("Updated menu:", initial_menu)
print("Availability:", check_item(initial_menu, "Pizza"))
