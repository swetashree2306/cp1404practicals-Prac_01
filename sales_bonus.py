# Intermediate Exercises

# 1
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales amount:$ "))
while sales > 0:
    if sales < 1000:
        bonus = ((sales/100) * 10) # 10% bonus
        print("salesman Bonus:$", bonus)

    elif sales > 1000:
        bonus = ((sales/100) * 15) # 15% bonus
        print("salesman Bonus:$", bonus)
    sales = float(input("Enter sales $: "))
else:
    print("Please enter a valid entry")



