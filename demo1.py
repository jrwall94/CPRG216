import math

num_people = int(input("Enter the number of people attending: "))

num_pizzas = math.ceil(((num_people) * 2) / 12)
price = num_pizzas * 18.75

print(f"You need to order {num_pizzas} for a cost of ${price}")