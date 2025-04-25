#Endrit Ngjelina
#SPC ID#2436798
#COP1000
#Worked alone
#This program prompts user to enter a two digit integer
#Then it prompts user to enter a different two digit integer
#And it calculates which integer is bigger and by how much

#User inputs the first two digit integer
number1 = int(input('Enter a two digit number: '))

#The nested if block calculates and displays the output in order
#If the input is correct, it displays the result
#If the input is incorrect, it displays an error message
if number1 >= 10 and number1 <= 99:
    number2 = int(input('Enter a different two digit number: '))
    if number2 < 10 or number2 > 99:
        print('Something is wrong with your second input. Please try again.')
    elif number2 == number1: 
        print('Something is wrong with your input. Please try again.')
    elif number1 < number2:
        print(f'{number2} is bigger than {number1} by {number2 - number1}.')
    else:
        print(f'{number1} is bigger than {number2} by {number1 - number2}.')
else:
    print('Something is wrong with your first input. Please try again.')
