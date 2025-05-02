'''
Exercise 33: Day Old Bread
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
'''
REG_PRICE = 3.49
DIS= 0.6

bread = int(input('Enter number of day old bread : '))

price = REG_PRICE * bread
disc = DIS * price
total = price - disc

print(f'Price:    $%5.2f.'%price)
print(f'Discount: $%5.2f.'%disc)
print(f'Total:    $%5.2f.'%total)
