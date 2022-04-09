"""
 Displays all of the odd numbers between
1 and 20 with a space between each one.
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
a. Count in 10s from 0 to 100
"""
for i in range(0, 110, 10):
    print(i, end=' ')
print()

"""
b. Count down from 20 to 1 
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
c. Ask the user for a number, then print that many stars (*), all on one line
"""
num = int(input("Enter the number of raw:"))
for i in range(num):
    print("*", end=" ")

"""
d. Print n lines of increasing stars. 
"""
num = int(input("enter no."))
for i in range(num + 1):
    print("*" * i)
