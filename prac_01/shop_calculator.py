DISCOUNT_REQUIREMENT = 100  # Total price needed for a discount
DISCOUNT_RATE = 0.1
ITEM_MIN = 0

total_price = 0
no_of_items = int(input("Number of items: "))
while no_of_items < ITEM_MIN:
    print("Invalid number of items!")
    no_of_items = int(input("Number of items: "))
for items in range(no_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > DISCOUNT_REQUIREMENT:
    total_price -= total_price * DISCOUNT_RATE
print(f"Total price for {no_of_items} items is ${total_price:.2f}")
