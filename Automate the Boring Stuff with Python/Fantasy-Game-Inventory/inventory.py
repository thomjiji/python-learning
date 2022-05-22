stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v, k, sep=' ')
        item_total += v
    print(f"Total number of items: {str(item_total)}")


def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1  # what inventory[i] returned is i.values(). i is keys.
    return inventory


inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)