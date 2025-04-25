#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#prompt user for distance in miles
#convert miles to kilometers
#1.609 kilometers is 1 mile
#Display distance in kilometers
#Create constant for kilometers
KILOMETERS = 1.609

#Input section
#user inputs distance in miles
distance= float(input("Enter the miles "))
#Processng Section
#The input is converted to miles by multiplying with 1.609/mile
result= distance * 1.609

#Output sectoin
#User receives the distance in kilometers
print(f'{distance:,.2f} miles is {result:,.3f} kilometers.')

#Worked Alone