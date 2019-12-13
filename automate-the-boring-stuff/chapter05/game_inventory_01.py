"""Fantasy Game Inventory

Print the inventory to the screen.
"""


def display_inventory(inventory):
    total = 0
    print("Inventory:\n=========")

    for k, v in inventory.items():
        print(v, k)
        total += v

    print("\nTotal number of items:", total)


stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
display_inventory(stuff)
