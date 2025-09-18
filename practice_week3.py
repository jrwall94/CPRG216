# Problem: Calculate the amount of tiles needed to cover a floor and the total cost

floor_width = int(input("What is the width of your floor in feet?\n> "))
floor_length = int(input("What is the length of your floor in feet?\n> "))
tile_size = int(input("How many square meters are your tiles?\n> "))
tile_price = int(input("What is the per-tile cost in dollars?\n> "))

tiles = (floor_width * floor_length) / tile_size
cost = tiles * tile_price

print("You will need", tiles, "tiles to cover your floor, costing you $", cost)