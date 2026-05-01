grocery_inventory = {"Milk": (113, "Dairy"), "Eggs": (116, "Dairy"), "Bread": (117, "Bakery"), "Apples": (141, "Produce")}
bread_details = grocery_inventory.get("Bread")
cookies_data = {"Cookies": (143, "Bakery")}
grocery_inventory.update(cookies_data)
print(f"Inventory after adding Cookies: {grocery_inventory}")
grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}")
print(f"Details of Bread: {bread_details}")