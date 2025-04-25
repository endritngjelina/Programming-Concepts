#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#prompt user to input numerator of fraction
#prompt user to input denominator of fraction
#express improper fraction as mixed number


#Input section
#The user inputs the numerator
#The user inputs the denominator
numerator=int(input("Enter the numerator "))
denominator=int(input("Enter the denominator "))
#Processing section
#Program calculates whole number
#Program calculates remainder
whole_number=numerator//denominator
remainder= numerator%denominator
#Output section
#Program displays mixed number
print(f'As a mixed number that is {whole_number} and {remainder}/{denominator}.')

#Worked Alone
