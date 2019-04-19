"""List to Dictionary Function for Fantasy Game Inventory

Add the list to the inventory(dict).
Print the inventory to the screen.
"""


def add_to_inventory(inventory, loot):
    for item in loot:
        # if item not in inventory add it and set its value to 0
        inventory.setdefault(item, 0)
        inventory[item] += 1


def display_inventory(inventory):
    total = 0
    print("Inventory:\n=========")

    # iterate over keys and values in the dict
    for k, v in inventory.items():
        print(v, k)
        total += v

    print("\nTotal number of items:", total)


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

add_to_inventory(stuff, loot)
display_inventory(stuff)
