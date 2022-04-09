
"""
CP1404/CP5632 - Practical
Pseudocode for Shop Calculator
"""
total_price = 0
items = int(input("Enter total number of items: "))
while items < 0:
    print("Invalid Entry")

for i in range(items):
    price = float(input("Enter the amount of items:"))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # 10% discount is applied

print("Total price for ", items, " items is $", total_price, sep='')
