

import copy   #for deep copy


#Given data

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}



#Task1-Explore the Menu
print("\n===== MENU =====")

#create an empty set to store all categories (set avoids duplicates)
categories = set()

#loop through each item in the menu
for item in menu:
    categories.add(menu[item]["category"])  #add the category

#print menu by category
#loop through each category
for cat in categories:
    print(f"\n===== {cat} =====")

    #loop again through all menu items
    for item in menu:
        if menu[item]["category"] == cat:   #if item belongs to this category
            price = menu[item]["price"]
            #check availability
            if menu[item]["available"]:
                status = "Available"  
            else:
                status = "Unavailable"

            print(f"{item:<15} ₹{price:<6.2f} [{status}]")

#total items on the menu using len
print("\nTotal items:", len(menu))

#available items count
available_count = 0
#loop through each item in the menu
for item in menu:
    if menu[item]["available"]: #check availability
        available_count += 1
print("Available items:", available_count)

#most expensive item
max_item = None
max_price = 0
#loop through each item in the menu
for item in menu:
    if menu[item]["price"] > max_price: #check if present item price greater than stored max price
        max_price = menu[item]["price"] #update the max price and max_item if above condition is true
        max_item = item
print(f"Most expensive: {max_item} ₹{max_price}")

#items under 150
print("\nItems under ₹150:")
#loop through each item in the menu
for item in menu:
    if menu[item]["price"] < 150: #check if item price is <150
        print(f"{item} ₹{menu[item]['price']}")


#Task2-Cart Operations

#create empty cart list (this will store all selected items)
cart = []

#function to add the item into cart
def add_item(name, qty):

    #first check if item exists in menu or not
    if name not in menu:
        print(f"{name} not found in menu")
        return

    #check if item is availabe or not
    if not menu[name]["available"]:
        print(f"{name} is unavailable")
        return

    #now check if item already present in cart
    #if yes, just increase the quantity instead of adding again
    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            print(f"Updated {name} quantity to {item['quantity']}")
            return

    #if item not present in cart, add as new entry
    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })
    print(f"Added {name}")

#function to remove item from cart
def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)   #remove item from list
            print(f"Removed {name}")
            return
    #if item not found in cart
    print(f"{name} not in cart")

#function to print current cart items
def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)

#simulate given steps
add_item("Paneer Tikka", 2)
print_cart()

add_item("Gulab Jamun", 1)
print_cart()

add_item("Paneer Tikka", 1)
print_cart()

add_item("Mystery Burger", 1)
print_cart()

add_item("Chicken Wings", 1)
print_cart()

remove_item("Gulab Jamun")
print_cart()

#Final order summary
print("\n========== Order Summary ==========")

subtotal = 0

#loop through cart and calculate total
for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:<20} x{item['quantity']:<3} ₹{total:>7.2f}")

#calculate gst and final amount
gst = subtotal * 0.05
total_pay = subtotal + gst

print("------------------------------------")
print(f"{'Subtotal:':<25} ₹{subtotal:>7.2f}")
print(f"{'GST (5%):':<25} ₹{gst:>7.2f}")
print(f"{'Total Payable:':<25} ₹{total_pay:>7.2f}")
print("====================================")


#Task3-Inventory Tracker with Deep Copy 
#create deep copy of inventory
inventory_backup = copy.deepcopy(inventory)

#modify one value
inventory["Paneer Tikka"]["stock"] = 5

print("\nInventory Changed:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

#restoring inventory back to original using backup
inventory = copy.deepcopy(inventory_backup)

#deduct stock based on cart
for item in cart:
    name = item["item"]
    qty = item["quantity"]

    #check if enough stock is available
    if inventory[name]["stock"] >= qty:
        inventory[name]["stock"] -= qty
    else:
        print(f"Warning: Not enough stock for {name}")
        inventory[name]["stock"] = 0

#reorder alert
print("\nReorder Alerts:")
for item in inventory:
     #check if stock is less than or equal to reorder level
    if inventory[item]["stock"] <= inventory[item]["reorder_level"]:
        stock = inventory[item]["stock"]
        reorder_level = inventory[item]["reorder_level"]
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder_level})")

#Print both inventory and inventory_backup
print("\n===== FINAL INVENTORY (AFTER UPDATES) =====")
for item in inventory:
    print(f"{item:<15} Stock: {inventory[item]['stock']}")

print("\n===== INVENTORY BACKUP (ORIGINAL DATA) =====")
for item in inventory_backup:
    print(f"{item:<15} Stock: {inventory_backup[item]['stock']}")

#Task4-Daily Sales Log Analysis

#Calculate revenue per day
print("\nRevenue per day:")
daily_revenue = {}  #to store date and total revenue

#loop through each date
for date in sales_log:
    total = 0

    #loop through all orders of that day
    for order in sales_log[date]:
        total += order["total"]
    daily_revenue[date] = total
    print(date, "₹", total)

#best-selling day 
best_day = max(daily_revenue, key=daily_revenue.get)
print("Best day:", best_day)

#most ordered item
item_count = {}

#loop through all orders in all dates
for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            #count how many times each item appears
            item_count[item] = item_count.get(item, 0) + 1

#get item with highest count
most_item = max(item_count, key=item_count.get)
print("Most ordered item:", most_item)

#add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

#print again
print("\nUpdated Revenue:")
for date in sales_log:
    total = sum(order["total"] for order in sales_log[date])
    print(date, "₹", total)

#best-selling day 
best_day = max(daily_revenue, key=daily_revenue.get)
print("Best day:", best_day)

#enumerate all orders
print("\nAll Orders:")
count = 1
for date in sales_log:
    for order in sales_log[date]:
        items = ", ".join(order["items"])   #join items into string
        print(f"{count}. [{date}] Order #{order['order_id']} - ₹{order['total']} - Items: {items}")
        count += 1