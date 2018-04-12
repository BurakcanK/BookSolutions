""" Fantasy Game Inventory

Prints the inventory to the screen.
"""

def displayInventory(inventory):
    total = 0
    print("\nInventory:\n=========")

    # iterate over keys and values in the dict
    for k, v in inventory.items():
        print(v, k)
        total += v

    print("\nTotal number of items:", total)

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
