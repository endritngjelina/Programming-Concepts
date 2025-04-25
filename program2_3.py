#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#input the unit price of item
#input the quantity of item
#multiply unit price with quantity to get subtotal
#multiply subtotal with constant to get sales tax
#add subtotal with sales tax to get total due
#display the subtotal, sales tax and total due


#input section
#User enters in price
num1=float(input("Enter the item's unit price "))

#User enters in quantity
num2=float(input("Enter the quantity "))

#Tax is 7% in Florida
TAX= 0.07

#processing section
#Calculate subtotal
subtotal= num1 * num2

#Calculate tax subtotal
sales_tax= TAX * subtotal
#Calculate total due
total_due= sales_tax + subtotal

#output section
#Display the subtotal
#Display sales tax
#Display the total due
print(format(f'Subtotal is ${subtotal:,.2f}.'))
print(f'Sales tax is ${sales_tax:,.2f}.')
print(f'The total due is ${total_due:,.2f}.')

#Worked Alone
